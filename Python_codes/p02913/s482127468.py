# -*- coding: utf-8 -*-
import sys
N=int(sys.stdin.readline().strip())
S=sys.stdin.readline().strip()
S=S[::-1]

dp=[ [ 0 for j in range(N+1) ] for i in range(N+1) ]

for i in range(1,N+1):  #iは1-indexed
    for j in range(1,i+1):
        if S[i-1]==S[j-1]:  #Sは0-indexedなので-1
            dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1)
        else:
            dp[i][j]=0

ans=0
for i in range(1,N+1):  #iは1-indexed
    for j in range(1,i):
        ans=max(ans,min(dp[i][j],i-j))  #2つの文字列は重ならないので最長でもi-j
print ans
