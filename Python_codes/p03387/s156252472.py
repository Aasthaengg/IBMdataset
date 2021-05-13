# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

A = lr()
A.sort()
lack = A[2] - A[0] + (A[2] - A[1])
answer = lack // 2
if lack&1:
    answer += 2
print(answer)
