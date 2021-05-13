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

x,a,b = map(int, read().split())
print('A' if abs(b-x)>abs(a-x) else 'B')