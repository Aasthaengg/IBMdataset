"""
author : halo2halo
date : 12, Jan, 2020
"""

import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b = readline().split()
print(0 if a < b else 10)
