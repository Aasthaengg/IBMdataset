# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
from math import gcd
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N=int(input())
    d=defaultdict(lambda:[0,0])
    zz=0
    for _ in range(N):
        a,b=map(int,input().split())
        g=gcd(a,b)
        if g==0:
            zz+=1
        else:
            a//=g
            b//=g
            if a<0:
                a*=-1
                b*=-1
            if a*b>0:
                d[(a,b)][0]+=1
            elif a*b<0:
                d[(-b,a)][1]+=1
            else:
                if a:
                    d[(1,0)][0]+=1
                else:
                    d[(1,0)][1]+=1
    l=[]
    other=0
    for k,a in d.items():
        if a[0] and a[1]:
            l.append((a[0],a[1]))
        else:
            other+=sum(a)
    ans=pow(2,other,MOD)
    ans%=MOD
    dp=[[0] for _ in range(len(l)+1)]
    dp[0]=1
    for i in range(len(l)):
        dp[i+1]=dp[i]*(pow(2,l[i][0],MOD)+pow(2,l[i][1],MOD)-1)
        dp[i+1]%=MOD
    ans*=dp[-1]
    ans-=1
    ans+=zz
    ans%=MOD
    print(ans)

if __name__ == '__main__':
    main()
