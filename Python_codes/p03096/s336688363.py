# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N=int(input())
C=[]
MAX=-1
for i in range(N):
    c=int1(input())
    MAX=max(MAX,c)
    if not C or (C and C[-1]!=c):
        C.append(c)
M=len(C)
dp=[0]*(M+1)
dp[0]=1
last=[-1]*(MAX+1)
for i in range(M):
    if last[C[i]]!=-1:
        dp[i+1]+=dp[i]+dp[last[C[i]]]
    else:
        dp[i+1]=dp[i]
    dp[i+1]%=MOD
    last[C[i]]=i+1
print(dp[-1])