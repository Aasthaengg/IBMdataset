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

A, B = map(int, read().split())
print(A + B if A + B < 10 else 'error')
