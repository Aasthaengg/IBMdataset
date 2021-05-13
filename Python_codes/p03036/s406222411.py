# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

R, D, X = lr()
for i in range(1, 11):
    X = R * X - D
    print(X)