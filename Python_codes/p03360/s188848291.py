# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

A = lr()
K = ir()
A.sort()
answer = sum(A[:2])
answer += pow(2, K) * A[2]
print(answer)
