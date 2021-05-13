# -*- coding: utf-8 -*-
import sys


L = input()
#%%
MOD = 10**9+7


dp = [[0]*2 for _ in range(len(L))]
dp[0][0] = 1
dp[0][1] = 2
for i,l in enumerate(L[1:]):
    dp[i+1][0] = (3*dp[i][0] + int(l)*dp[i][1])%MOD
    dp[i+1][1] = ((1+int(l))*dp[i][1])%MOD
print((dp[-1][0]+dp[-1][1])%MOD)