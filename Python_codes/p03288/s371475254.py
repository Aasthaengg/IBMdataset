"""
author : halo2halo
date : 23, Jan, 2020
"""

import sys

# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

R = int(readline())
print('ABC' if R < 1200 else 'ARC' if R < 2800 else 'AGC')
