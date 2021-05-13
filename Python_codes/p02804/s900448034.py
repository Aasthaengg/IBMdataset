MOD=10**9+7
def facinv(N):
    fac,finv,inv=[0]*(N+1),[0]*(N+1),[0]*(N+1)
    fac[0]=1;fac[1]=1;finv[0]=1;finv[1]=1;inv[1]=1
    for i in range(2,N+1):
        fac[i]=fac[i-1]*i%MOD
        inv[i]=MOD-inv[MOD%i]*(MOD//i)%MOD
        finv[i]=finv[i-1]*inv[i]%MOD
    return fac,finv,inv
def COM(n,r):
    if n<r or r<0:
        return 0
    else:
        return ((fac[n]*finv[r])%MOD*finv[n-r])%MOD
        
N,K=map(int,input().split())
A=sorted(map(int,input().split()))
fac,finv,inv=facinv(N)
ans=0
for i in range(N):
    if(i>0):
        ans=(ans+(A[i]*COM(i,K-1)%MOD))%MOD
    if(i<N-1):
        ans=(ans-(A[i]*COM(N-i-1,K-1)%MOD))%MOD
print(ans)