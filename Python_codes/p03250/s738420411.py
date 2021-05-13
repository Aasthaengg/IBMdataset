# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

A = lr()
A.sort()
answer = sum(A) + 9 * max(A)
print(answer)
