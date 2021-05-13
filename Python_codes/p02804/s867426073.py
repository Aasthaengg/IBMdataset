n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()

def mod_nCr(n,k,mod):
    r = min(k,n-k)
    return fact[n]*factinv[k]*factinv[n-k]%mod

mod = 10**9+7
fact = [1,1]
inv = [0,1]
factinv = [1,1]
for i in range(2,n+1):
    fact.append(fact[-1]*i%mod)
    inv.append((-inv[mod%i]*(mod//i))%mod)
    factinv.append((factinv[-1]*inv[-1])%mod)
    
ans = 0
for i in range(k-1,n)[::-1]:
    ans += a[i]*mod_nCr(i,k-1,mod)
    ans %= mod
a.reverse()
for i in range(k-1,n)[::-1]:
    ans -= a[i]*mod_nCr(i,k-1,mod)
    ans %= mod
print(ans%mod)