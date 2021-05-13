import sys
N,M,K=map(int, sys.stdin.readline().split())
mod=998244353

fact, inv_fact=[1], [1]
fact_tmp=1
for i in range(1, N+1):
    fact_tmp*=i
    fact_tmp%=mod
    fact.append(fact_tmp)
    inv_fact.append(pow(fact_tmp, mod-2, mod))

def ncr(n,r):
	if n<0 or r<0 or n<r:	return 0
	else:   return (fact[n]*inv_fact[r]*inv_fact[n-r])%mod

ans=0
for k in range(K+1):
    ans+=ncr(N-1,k)*M*pow(M-1,N-1-k,mod)
    ans%=mod
print ans