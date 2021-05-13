#!/usr/bin/ python3.8
# K   : 青
# N-K : 赤

MOD=10**9+7
M=10**6
fac=[1]*M
ifac=[1]*M
inv=[1]*M
for i in range(2,M):
    fac[i]=i*fac[i-1]%MOD
    inv[i]=MOD-(MOD//i)*inv[MOD%i]%MOD
    ifac[i]=inv[i]*ifac[i-1]%MOD

def comb(n,k):
    if n<0 or n-k<0 or k<0:
        return 0
    return fac[n]*ifac[n-k]%MOD*ifac[k]%MOD

N,K=map(int,input().split())
R=N-K

for i in range(1,K+1):
    ans=comb((K-i)+i-1,(K-i))*comb((R-(i-1))+i,i)%MOD
    print(ans)