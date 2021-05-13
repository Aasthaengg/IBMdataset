# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

A, B, C = lr()
bl = (A+B) >= C
print('Yes' if bl else 'No')
