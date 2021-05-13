# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:14:09 2020

@author: Kanaru Sato
"""
import itertools

h,w = list(map(int, input().split()))
mod = 10**9+7
Map = []
for i in range(h):
    Map.append(list(input()))

dp = [[0 for i in range(w)] for j in range(h)]

for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            dp[i][j] = 1
        else:
            if Map[i][j] == "#":
                dp[i][j] = -1
            else:
                if i-1 >= 0 and dp[i-1][j] != -1:
                    dp[i][j] += dp[i-1][j]
                if j-1 >= 0 and dp[i][j-1] != -1:
                    dp[i][j] += dp[i][j-1]
                dp[i][j] %= mod

print(dp[h-1][w-1])