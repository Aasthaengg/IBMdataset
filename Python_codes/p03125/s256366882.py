"""
author : halo2halo
date : 15, Jan, 2020
"""

import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

A, B = map(int, readline().split())
print(A + B if B % A == 0 else B - A)
