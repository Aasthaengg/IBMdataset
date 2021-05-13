#!/usr/bin/env python3

n, k = [int(i) for i in input().split(' ')]

arr = [int(i) for i in input().split(' ')]

dp = [10**10]*n

k += 1
dp[0] = 0

for i in range(0, n):
    for j in range(1, k):
        if i+j < n:
            dp[i+j] = min(dp[i+j], dp[i] + abs(arr[i+j]-arr[i]))

print(dp[n-1])
