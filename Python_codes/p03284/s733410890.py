"""
author : halo2halo
date : 23, Jan, 2020
"""

import sys

# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, K = map(int, readline().split())
print(0 if N//K*K==N else 1)
