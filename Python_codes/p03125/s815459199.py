# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

A, B = lr()
bl = B % A == 0
print(A + B if bl else B - A)
