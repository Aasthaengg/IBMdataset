# ABC 132 D

N=10**4
p=10**9+7
f,finv,inv=[0]*(N+5),[0]*(N+5),[0]*(N+5)

def nCr_init(L,p):
    for i in range(L+1):
        if i<=1:
            f[i],finv[i],inv[i]=1,1,1
        else:
            f[i]=(f[i-1]*i)%p
            inv[i]=(p-inv[p%i]*(p//i))%p
            finv[i]=(finv[i-1]*inv[i])%p

def nCr(n,r,p):
    if 0<=r<=n and 0<=n:
        return (f[n]*finv[n-r]*finv[r])%p
    else:
        return 0
    
nCr_init(N,p)

N,K=map(int,input().split())
for i in range(1,K+1):
    NR=N-K
    NB=K
    print((nCr(NB-1,i-1,p)*nCr(NR+1,i,p))%p)