n,k=map(int,input().split())
mod=1000000007

fac = [1]*(n+1)
inv = [1]*(n+1)
for i in range(2,n+1):
    fac[i] = fac[i-1]*i % mod
    inv[i] = pow(fac[i],mod-2,mod)

def nCk(n,k):
    return fac[n]*inv[k]%mod*inv[n-k]%mod
ans = 0
for i in range(min(k+1,n)):
    ans += nCk(n,i)*nCk(n-1,i)%mod
    ans %=mod
print(ans)