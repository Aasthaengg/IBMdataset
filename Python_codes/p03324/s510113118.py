# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

D, N = lr()
if N == 100:
    N += 1
answer = 100 ** D * N
print(answer)
