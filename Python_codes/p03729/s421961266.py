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

A, B, C = readline().decode('utf8').split()

print('YES' if A[-1] == B[0] and B[-1] == C[0] else 'NO')
