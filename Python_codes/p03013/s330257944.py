#!/usr/bin/env python
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]
mod = 1000000007

dp = [-1 for _ in range(n)]
for i in range(m):
    dp[a[i]-1] = 0 

if n == 1:
    print(1)
    exit()
if n == 2:
    if m == 0:
        print(2)
        exit()
    elif m == 1:
        print(1)
        exit()

if dp[0] != 0:
    dp[0] = 1 
if dp[1] != 0:
    dp[1] = dp[0]+1

for i in range(2, n): 
    if dp[i] == 0:
        continue
    dp[i] = (dp[i-1] + dp[i-2])%mod

print(dp[n-1])
