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

H, W = map(int, read().split())

print('GREATER' if H>W else 'LESS' if H<W else 'EQUAL')
