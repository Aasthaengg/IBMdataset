# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, X = lr()
M = [ir() for _ in range(N)]
M.sort()
answer = N
X -= sum(M)
answer += X // M[0]
print(answer)
