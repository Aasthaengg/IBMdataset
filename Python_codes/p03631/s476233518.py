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

x = readline().decode('utf8').rstrip()
print('Yes' if x == x[::-1] else 'No')
