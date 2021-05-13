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

a,b,c = map(int, readline().decode('utf8').split())

print('YES' if 2 * b == a + c else 'NO')
