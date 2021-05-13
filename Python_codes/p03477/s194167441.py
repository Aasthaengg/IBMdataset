"""
author : halo2halo
date : 24, Jan, 2020
"""

import sys
import itertools

# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B, C, D = map(int, readline().split())

print('Left' if A + B > C + D else 'Balanced' if A + B == C + D else 'Right')
