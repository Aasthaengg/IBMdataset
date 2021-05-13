# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

R,C,K=map(int,input().split())
V=[[0]*C for _ in range(R)]
for i in range(K):
    r,c,v=map(int,input().split())
    r-=1
    c-=1
    V[r][c]=v
dp=[[0]*C for _ in range(4)]
for y in range(R):
    for x in range(C):
        for i in range(2,-1,-1):
            dp[i+1][x]=max(dp[i+1][x],dp[i][x]+V[y][x])
        if x<C-1:
            for i in range(3,-1,-1):
                dp[i][x+1]=max(dp[i][x+1],dp[i][x])
    if y+1<R:
        MAX=0
        for x in range(C):
            for i in range(4):
                MAX=max(MAX,dp[i][x])
                dp[i][x]=0
            dp[0][x]=MAX
print(max(dp[0][-1],dp[1][-1],dp[2][-1],dp[3][-1]))