# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

a, b, c, d = lr()
bl = abs(a - c) <= d
if abs(a - b) <= d and abs(b - c) <= d:
    bl = True
print('Yes' if bl else 'No')
