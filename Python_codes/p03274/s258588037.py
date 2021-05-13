# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K = lr()
X = lr()
answer = []
for i in range(N-K+1):
    l = X[i]; r = X[i+K-1]
    a = abs(l) + abs(r-l)
    b = abs(r) + abs(l-r)
    answer.append(min(a, b))

print(min(answer))
# 03