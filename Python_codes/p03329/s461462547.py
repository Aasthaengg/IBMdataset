# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# dp
N = ir()
INF = 10 ** 8
dp = [INF] * (N+1)
dp[0] = 0
for i in range(5, 0, -1):
    num = 9 ** i
    for j in range(N):
        if j+num <= N:
            dp[j+num] = min(dp[j+num], dp[j]+1)

for i in range(6, 0, -1):
    num = 6 ** i
    for j in range(N):
        if j+num <= N:
            dp[j+num] = min(dp[j+num], dp[j]+1)

num = 1
for j in range(N):
    dp[j+num] = min(dp[j+num], dp[j]+1)

answer = dp[N]
print(answer)
