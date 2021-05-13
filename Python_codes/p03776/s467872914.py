# -*- coding: utf-8 -*-
import sys
from bisect import bisect_left,bisect_right
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**18+3
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N,A,B=map(int,input().split())
    v=list(map(int,input().split()))
    v.sort()
    ans=0
    for i in range(A,B+1):
        ans=max(ans,sum(v[-i:])/i)
    def COMinit(n,MOD):
        fac,finv,inv=[0]*max(2,n+1),[0]*max(2,n+1),[0]*max(2,n+1)
        fac[0]=fac[1]=1
        finv[0]=finv[1]=1
        inv[1]=1
        for i in range(2,(n+1)):
            fac[i]=fac[i-1]*i%MOD
            inv[i]=MOD-inv[MOD%i]*(MOD//i)%MOD
            finv[i]=finv[i-1]*inv[i]%MOD
        return fac,finv,inv
    
    fac,finv,inv=COMinit(N,MOD)
    
    def COM(n, k, MOD=MOD):
        if n<k or n<0 or k<0:
            return 0
        return fac[n]*(finv[k]*finv[n-k]%MOD)%MOD
    ans2=0
    for i in range(A,B+1):
        if sum(v[-i:])/i==ans:
            x=v[-i]
            n=bisect_right(v,x)-bisect_left(v,x)
            m=bisect_right(v,x)-(N-i)
            ans2+=COM(n,m)
    print(ans)
    print(ans2)

if __name__ == '__main__':
    main()
