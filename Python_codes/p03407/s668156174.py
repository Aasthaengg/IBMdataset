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

N, A, C = map(int, readline().split())

print('Yes' if N + A >= C else 'No')
