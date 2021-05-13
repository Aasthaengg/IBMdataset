"""
author : halo2halo
date : 24, Jan, 2020
"""

import sys

# import itertools
# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

X, A, B = map(int, read().split())
print((X-A)%B)