import numpy as np

MOD=1000000007

n,k=map(int,input().split())
k=min(k,n-1)
fac=np.zeros((n+1)).astype(np.int64)
invfac=np.zeros((n+1)).astype(np.int64)
inv=np.zeros((n+1)).astype(np.int64)

invfac[0]=fac[0]=invfac[1]=fac[1]=inv[1]=1
for i in range(2,n+1):
    fac[i]=(fac[i-1]*i)%MOD
    inv[i]=(-inv[MOD%i]*(MOD//i))%MOD
    invfac[i]=(invfac[i-1]*inv[i])%MOD
def nCr(n,r):
    return ((fac[n]*invfac[r]%MOD)*invfac[n-r])%MOD
def nHr(n,r):
    return nCr(n+r-1,r)
    
print(np.sum(nCr(n,np.arange(k+1))*nHr(n-np.arange(k+1), np.arange(k+1))%MOD)%MOD)
