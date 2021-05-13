"""
author : halo2halo
date : 24, Jan, 2020
"""

import sys

# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, c, d = map(int, readline().split())

if abs(c - a) <= d:
    bl = True
elif abs(b - a) <= d and abs(c - b) <= d:
    bl = True
else:
    bl = False
print("Yes" if bl else "No")
