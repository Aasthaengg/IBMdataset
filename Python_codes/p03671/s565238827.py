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

a = [int(i) for i in readline().split()]
a.sort()
print(sum(a[:2]))