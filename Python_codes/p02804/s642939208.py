#E
N,K=map(int,input().split())
A=list(map(int,input().split()))
mod=10**9+7
ans=0

fact=[1 for i in range(N+1)]
for i in range(2,N+1):
    fact[i]=(fact[i-1]*i)%mod
    
fact_inv=[1 for i in range(N+1)]
for i in range(2,N+1):
    fact_inv[i]=pow(fact[i],mod-2,mod)

def nCk(n,k):
    re=(fact[n]*fact_inv[n-k]*fact_inv[k])%mod
    return re

ans=0
A=sorted(A)
for i in range(K-1,N):
    ans+=nCk(i,K-1)*(A[i]-A[N-i-1])
    ans%=mod
    
print(ans)