"""
author : halo2halo
date : 24, Jan, 2020
"""

import sys

# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B, C = map(int, readline().split())

print('YES' if A <= C <= A + B else 'NO')
