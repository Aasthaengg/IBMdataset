n,k = map(int,input().split())
mod = 10**9+7
ans = [0]*(k+1)
fac = [0]*(n+1)
inv = [0]*(n+1)
def comb(n,k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n]*inv[k]%mod*inv[n-k]%mod
fac[0] = inv[0] = 1
for i in range(1,n+1):
    fac[i] = fac[i-1]*i%mod
    inv[i] = pow(fac[i],mod-2,mod)
for i in range(1,k+1):
    ans = comb(n-k+1,i)%mod*comb(k-1,i-1)%mod
    print(ans)