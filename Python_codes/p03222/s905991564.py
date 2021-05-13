# -*- coding: utf-8 -*-
import sys
from collections import deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    H,W,K=map(int,input().split())
    dpdp=[[0]*2 for _ in range(W)]
    dpdp[0][0]=1
    for i in range(W-1):
        dpdp[i+1][0]=dpdp[i][0]+dpdp[i][1]
        dpdp[i+1][1]=dpdp[i][0]
    
    dp=[[0]*W for _ in range(H+1)]
    dp[0][0]=1
    for i in range(H):
        for j in range(W):
            if j==0 or j==W-1:
                dp[i+1][j]+=dp[i][j]*(sum(dpdp[W-2]))
            else:
                dp[i+1][j]+=dp[i][j]*(sum(dpdp[max(j-1,0)])*sum(dpdp[max(W-2-j,0)]))
            dp[i+1][j]%=MOD
            if j<=W-2:
                dp[i+1][j+1]+=dp[i][j]*(sum(dpdp[max(j-1,0)])*sum(dpdp[max(W-3-j,0)]))
                dp[i+1][j+1]%=MOD
            if j>=1:
                dp[i+1][j-1]+=dp[i][j]*(sum(dpdp[max(j-2,0)])*sum(dpdp[max(W-2-j,0)]))
                dp[i+1][j-1]%=MOD
    print(dp[-1][K-1])

if __name__ == '__main__':
    main()
