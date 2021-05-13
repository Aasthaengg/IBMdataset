k=int(input())
s=input()

U=2*10**6+1
mod=10**9+7

fact=[1]*(U+1)
fact_inv=[1]*(U+1)

for i in range(1,U+1):
    fact[i]=(fact[i-1]*i)%mod
fact_inv[U]=pow(fact[U],mod-2,mod)

for i in range(U,0,-1):
	fact_inv[i-1]=(fact_inv[i]*i)%mod

def comb(n,k):
    if k<0 or k>n:
        return 0
    x=fact[n]
    x*=fact_inv[k]
    x%=mod
    x*=fact_inv[n-k]
    x%=mod
    return x
m=len(s)
ans=0
for i in range(k+1):
    ans=(ans+pow(25,i,mod)*comb(m+i-1,m-1)*pow(26,k-i,mod))%mod
print(ans)