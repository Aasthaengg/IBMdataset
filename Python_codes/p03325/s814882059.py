# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
A = np.array(lr())
answer = 0
while np.any(A%2==0):
    answer += (A%2==0).sum()
    A[A%2==0] //= 2

print(answer)
