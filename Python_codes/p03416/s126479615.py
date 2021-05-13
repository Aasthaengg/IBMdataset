# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

A, B = lr()
answer = sum(str(x) == str(x)[::-1] for x in range(A, B+1))
print(answer)
