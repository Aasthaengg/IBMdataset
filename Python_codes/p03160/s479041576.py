#!/usr/bin/env python3

n = int(input())

arr = [int(i) for i in input().split(' ')]

dp = [10**10]*n

dp[0] = 0

for i in range(0, n):
    for j in range(1, 3):
        if i+j < n:
            dp[i+j] = min(dp[i+j], dp[i] + abs(arr[i+j]-arr[i]))

print(dp[n-1])
