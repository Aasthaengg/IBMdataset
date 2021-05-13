K=int(input())
s=input()
S=len(s)
mod=10**9+7
MAX_N=10**7
fact=[1]
fact_inv=[0]*(MAX_N+4)
for i in range(MAX_N+3):
  fact.append(fact[-1]*(i+1)%mod)

fact_inv[-1]=pow(fact[-1],mod-2,mod)
for i in range(MAX_N+2,-1,-1):
  fact_inv[i]=fact_inv[i+1]*(i+1)%mod

def mod_comb_k(n,k,mod):
  return fact[n]*fact_inv[k]%mod*fact_inv[n-k] %mod

cnt=0
for i in range(K+1):
  a=(pow(26,i,mod)*pow(25,K-i,mod))*(mod_comb_k(K+S-i-1,S-1,mod))
  a%=mod
  cnt+=a
  cnt%=mod
print(cnt)