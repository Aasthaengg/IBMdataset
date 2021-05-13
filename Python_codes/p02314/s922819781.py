#!/usr/bin/env python2
# coding: utf-8

n, m = map(int, raw_input().split())
c = map(int, raw_input().split())

dp = ['inf'] * 50001
dp[0] = 0;

for i in range(m):
    for j in range(n+1):
        if j + c[i] > n:
            break
        else:
            dp[j + c[i]] = min(dp[j + c[i]], dp[j] + 1)

print dp[n]

