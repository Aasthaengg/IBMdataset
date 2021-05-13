# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 16:32:55 2020

@author: tinku
"""
n=int(input())
arr=list(map(float,input().split()))
dp=[[0 for j in range(n+1)] for i in range(n+1)]
dp[0][0]=1.0
for i in range(1,n+1):
    for j in range(n+1):
        if j==0:
            dp[i][j]=(1.0-arr[i-1])*dp[i-1][j]
        else:
            dp[i][j]=arr[i-1]*dp[i-1][j-1]+(1.0-arr[i-1])*dp[i-1][j]
print(sum(dp[n][n//2+1:]))