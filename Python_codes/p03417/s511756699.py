# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M = lr()
if N > M:
    N, M = M, N
if N == 1:
    if M == 1:
        answer = 1
    else:
        answer = M - 2
else:
    answer = (N-2) * (M-2)

print(answer)
