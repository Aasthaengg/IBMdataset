"""
author : halo2halo
date : 31, Jan, 2020
"""

import sys

# import itertools
# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b = read().decode('utf8').split()

print('H' if a==b else 'D')
