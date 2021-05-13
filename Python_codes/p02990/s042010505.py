MOD=10**9+7
def com(n,k,mod):
    res=1
    tmp=1
    for i in range(1,k+1):
        res=res*(n-i+1)%mod
        tmp=tmp*i%mod
    a=pow(tmp,mod-2,mod)
    return res*a%mod

N,K=map(int,input().split())
X=N-K

for i in range(1,K+1):
    print(com(X+1,i,MOD)*com(K-1,i-1,MOD)%MOD)