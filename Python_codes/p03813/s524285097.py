"""
author : halo2halo
date : 31, Jan, 2020
"""

import sys
import itertools

# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x = int(readline())
print('ABC' if x<1200 else 'ARC')