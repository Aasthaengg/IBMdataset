"""
author : halo2halo
date : 24, Jan, 2020
"""

import sys

# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b = map(int, readline().split())
print(':(' if a > 8 or b > 8 else 'Yay!')
