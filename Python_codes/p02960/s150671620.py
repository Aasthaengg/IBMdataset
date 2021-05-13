# -*- coding: utf-8 -*-
import sys
S=sys.stdin.readline().strip()
N=len(S)
mod=10**9+7
S=S[::-1]

dp=[ [ 0 for j in range(13) ] for i in range(N) ]

for i,x in enumerate(S):  #i桁目
    if i==0:
        num=pow(10,i,13)
        if x!="?":
            x=int(x)
            dp[i][(x*num)%13]=1
        else:
            for x in range(10):
                dp[i][(x*num)%13]=1
    else:
        num=pow(10,i,13)
        if x!="?":
            x=int(x)
            for j in range(13):
                n=(x*num+j)%13
                dp[i][n]+=dp[i-1][j]
                dp[i][n]%=mod
        else:
            for j in range(13):
                for x in range(10):
                    n=(x*num+j)%13
                    dp[i][n]+=dp[i-1][j]
                    dp[i][n]%=mod
print dp[N-1][5]%mod
