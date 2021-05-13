"""
author : halo2halo
date : 29, Jan, 2020
"""

import sys
import itertools

# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B = map(int, readline().split())

print('Possible' if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0 else 'Impossible')
