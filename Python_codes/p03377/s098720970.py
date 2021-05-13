# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

A, B, X = lr()
bl = A <= X <= A + B
print('YES' if bl else 'NO')
