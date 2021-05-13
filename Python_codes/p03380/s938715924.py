# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
A = lr()
A.sort()
first = A[-1]
second = max((min(x, first-x), x) for x in A[:-1])
print(first, second[1])
