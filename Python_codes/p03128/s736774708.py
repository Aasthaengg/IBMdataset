# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M = lr()
A = lr()
dp = [-1] * (N+1)
dp[0] = 0
match = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for x in range(N):
    for a in A:
        y = match[a]
        if x + y > N:
            continue
        dp[x+y] = max(dp[x+y], dp[x] * 10 + a)

answer = dp[N]
print(answer)
# 32