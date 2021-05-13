n,m,k = map(int,input().split())
mod = 998244353
def comb(n,k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n]*finv[k]%mod*finv[n-k]%mod
fac = [0]*(n+1)
finv = [0]*(n+1)
fac[0] = finv[0] = 1
for i in range(1,n+1):
    fac[i] = fac[i-1]*i%mod
    finv[i] = pow(fac[i],mod-2,mod)

ans = 0
for i in range(k+1):
    ans = (ans + m*comb(n-1,i)%mod*pow(m-1,n-1-i,mod)%mod)%mod
print(ans)