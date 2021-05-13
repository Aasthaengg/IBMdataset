"""
author : halo2halo
date : 15, Jan, 2020
"""

import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

H, W, h, w = map(int, read().split())
print((H - h) * (W - w))
