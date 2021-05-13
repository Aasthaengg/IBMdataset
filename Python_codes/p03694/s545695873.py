"""
author : halo2halo
date : 30, Jan, 2020
"""

import sys
import itertools

# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,*A = map(int, read().split())
A.sort()
print(A[-1]-A[0])
