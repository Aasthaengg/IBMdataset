# -*- coding: utf-8 -*-
"""
Created on Tue May  5 00:32:28 2020

@author: Kanaru Sato
"""

n = int(input())
p = list(map(float,input().split()))

dp = [[-1 for i in range(n+1)] for j in range(n)]

for i in range(n,0,-1):
    index = i-1
    for j in range(n-i+2):
        if index == n-1 and j == 0:
            dp[index][j] = 1-p[n-1]
        elif index == n-1 and j == 1:
            dp[index][j] = p[n-1]
        elif j == 0:
            dp[index][j] = dp[index+1][j]*(1-p[index])
        elif 1 <= j and j <= n-i:
            dp[index][j] = dp[index+1][j]*(1-p[index]) + dp[index+1][j-1]*(p[index])
        else:
            dp[index][j] = dp[index+1][j-1]*(p[index])

ans = 0
for j in range(n//2+1,n+1):
    ans += dp[0][j]

print(ans)