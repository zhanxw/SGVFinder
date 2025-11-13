from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import shutil
import numpy as np
import glob
import os

ext_modules = [Extension("gem_qa", ["gem_qa.pyx"], include_path = [np.get_include(), './'], include_dirs = [np.get_include(), './'], 
                         language = 'c++', extra_compile_args=["-std=c++11"], extra_link_args=["-std=c++11"]),\
               Extension("CSeqDict", ["CSeqDict.pyx"], include_path = ['./'], include_dirs = [], language = 'c++', extra_compile_args=["-std=c++11"],
                         extra_link_args=["-std=c++11"]),
               Extension("Delta", ["Delta.pyx"])]
setup(cmdclass={'build_ext': build_ext}, ext_modules=ext_modules)

# Find the built .so files and copy them to the current directory
build_lib = glob.glob('build/lib.*')
if build_lib:
    for so_file in ['gem_qa', 'CSeqDict', 'Delta']:
        so_paths = glob.glob(os.path.join(build_lib[0], so_file + '*.so'))
        if so_paths:
            shutil.copy(so_paths[0], so_file + '.so')