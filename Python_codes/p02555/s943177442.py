def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p


MOD = 10**9 + 7
N = 10**6
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

s = int(input())

ans = 0
for i in range(1, s // 3 + 1):
    rest = s - 3 * i
    ans += cmb(rest + i - 1, rest, MOD)

print(ans % MOD)