# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:20:35 2020
"""

import sys
import numpy as np

sys.setrecursionlimit(10 ** 9)
#def input():
#    return sys.stdin.readline()[:-1]
mod = 10**9+7

#N = int(input())
N, K = map(int,input().split())
A = np.array(list(map(int,input().split())))

dp = [True for i in range(K + 1)]
for i in range(K, -1, -1):
    if dp[i]:
        for a in A:
            if i - a >= 0:
                dp[i - a] = False

#    print(i, dp[i],A+i,dp[A+i])
#print(dp)

if dp[0]:
    ans = 'Second'
else:
    ans = 'First'
print(ans)