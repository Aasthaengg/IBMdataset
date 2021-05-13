N,M,K=map(int,input().split())
mod=998244353
P=[1 for i in range(10**6+1)]
for i in range(10**6):
  P[i+1]=P[i]*(i+1)%mod

def comb(a,b):
    if a>=b:
        return P[a]*pow(P[a-b],mod-2,mod)*pow(P[b],mod-2,mod)%mod
    else:
        return 0
ans=0
for i in range(K+1):
  ans+=M*comb(N-1,i)*pow(M-1,N-1-i,mod)
  ans%=mod
print(ans)