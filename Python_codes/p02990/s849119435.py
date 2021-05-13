def cmb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % mod
mod = 10**9 + 7
n , k = map(int,input().split())

fact = [1, 1]
factinv = [1, 1]
inv = [0,1]

for i in range(2,n+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((inv[mod % i] * (mod - (mod // i))) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

for i in range(k):
    ans = 1
    ans *= cmb(k-1,i,mod)
    ans *= cmb(n-k+1,i+1,mod)
    ans %= mod
    print(ans)