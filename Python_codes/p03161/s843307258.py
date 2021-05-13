#!/usr/bin/env python3

N, K = map(int, input().split())
H = list(map(int, input().split()))

if N <=K:
    print(abs(H[0]-H[-1]))
    exit()


dp = [float('inf') for _ in range(N+K+1)]

dp[0] = 0

for i in range(1, K+1):
    dp[i] = abs(H[0] - H[i])

for i in range(N):
    for j in range(i+1, i+K+1):
        if j < N:
            dp[j] = min(dp[i] + abs(H[i]-H[j]), dp[j])

print(dp[N-1])

