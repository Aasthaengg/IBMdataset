# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    S=[0]*(N+1)
    d=defaultdict(int)
    d[0]+=1
    ans=0
    for i in range(N):
        S[i+1]=(S[i]+A[i])%M
        ans+=d[S[i+1]]
        d[S[i+1]]+=1
    print(ans)

if __name__ == '__main__':
    main()
