import sys
input = sys.stdin.readline
from collections import *

S = input()[:-1]
L = len(S)
dp = [[0]*2 for _ in range(L+1)]
dp[0][0] = 1
MOD = 10**9+7

for i in range(L):
    if S[i]=='0':
        dp[i+1][0] = dp[i][0]%MOD
        dp[i+1][1] = 3*dp[i][1]%MOD
    else:
        dp[i+1][0] = 2*dp[i][0]%MOD
        dp[i+1][1] = (dp[i][0]+3*dp[i][1])%MOD
    
print(sum(dp[L])%MOD)