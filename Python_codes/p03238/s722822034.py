"""
author : halo2halo
date : 22, Jan, 2020
"""

import sys

# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
if N == 1:
    print("Hello World")
else:
    A, B = map(int, read().split())
    print(A + B)
