n, k = map(int,input().split())

mod = 10**9+7
MOD = 10 ** 9 + 7
MAX = 2*n+1


fact = [1] * (MAX + 1)  # i!
finv = [1] * (MAX + 1)  # (i!)^{-1}
iinv = [1] * (MAX + 1)  # i^{-1}

for i in range(2, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD
    iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * iinv[i] % MOD


def c(n, k):
    if n < k or n < 0 or k < 0:
        return 0
    return (fact[n] * finv[k] % MOD) * finv[n - k] % MOD


ans = 0
for m in range(1,min(n-1,k)+1):
    # print((c(n,m) * c(n-1,m)) % mod)
    ans += (c(n,m)%mod * c(n-1,m)%mod) % mod

if k == 1:
    print(ans % mod)

else:
    print((ans+1) % mod)


