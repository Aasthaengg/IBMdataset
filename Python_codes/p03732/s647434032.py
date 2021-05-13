# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N,W=map(int,input().split())
    w,v=[0]*N,[0]*N
    for i in range(N):
        w[i],v[i]=map(int,input().split())
    if w[0]>3*N:
        w0=w[0]
        W=min(W//w0*(3*N+1)+min(W%w0,3*N),(3*N+4)*N)
        for i in range(N):
            w[i]-=w0
            w[i]+=3*N+1
    dp=[[0]*(W+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            dp[i+1][j]=max(dp[i+1][j],dp[i][j])
            if j-w[i]>=0:
                dp[i+1][j]=max(dp[i+1][j],dp[i][j-w[i]]+v[i])
    print(dp[-1][-1])

if __name__ == '__main__':
    main()
