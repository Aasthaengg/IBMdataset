"""
author : halo2halo
date : 24, Jan, 2020
"""

import sys

# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, c, d = map(int, read().split())
print(min(a, b) + min(c,d))
