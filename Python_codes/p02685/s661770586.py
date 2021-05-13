n, m, k = map(int, input().split())

MOD = 998244353

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = MOD
N = 2 * 10 ** 5 + 10
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

res = 0
for i in range(k + 1):
    res += m * pow(m - 1, n - i - 1, MOD) * cmb(n - 1, i, MOD)
    res %= MOD

res %= MOD
print(res)