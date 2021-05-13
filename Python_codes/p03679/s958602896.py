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

X,A,B = map(int,readline().split())

print('delicious' if B-A<=0 else 'safe' if B-A<=X else 'dangerous')
