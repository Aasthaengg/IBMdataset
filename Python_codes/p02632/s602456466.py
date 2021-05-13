K=int(input())
S=input()
N=len(S)
mod=10**9+7

fact=[1]*(K+N)
for i in range(2,K+N):
    fact[i]=fact[i-1]*i%mod

inv=[1]*(K+N)
inv[K+N-1]=pow(fact[K+N-1],mod-2,mod)
for i in range(K+N-2,0,-1):
    inv[i]=inv[i+1]*(i+1)%mod
    
def comb(n,r):
    ret=fact[n]*inv[r]*inv[n-r]%mod
    return ret

ans=0
for i in range(K+1):
    ans+=pow(26,i,mod)*pow(25,K-i,mod)*comb(K+N-1-i,N-1)
    ans%=mod

print(ans)