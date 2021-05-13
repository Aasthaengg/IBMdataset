"""
author : halo2halo
date : 16, Jan, 2020
"""

import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

T, X = map(int, readline().decode('utf8').split())
print(T/X)
