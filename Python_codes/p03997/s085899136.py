"""
author : halo2halo
date : 2, Feb, 2020
"""

import sys
import itertools

import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a,b,h=map(int, read().split())
print(h*(b+a)//2)
