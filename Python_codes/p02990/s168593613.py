def binom(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)

    res = factinv[r] % p
    for i in range(r):
        res = res * (n - i) % p

    return fact[n] * factinv[r] * factinv[n-r] % p

N, K = list(map(int, input().split()))

p = 10 ** 9 + 7

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

for i in range(1, K + 1):
    print(binom(K - 1, i - 1) * binom(N - K + 1, i) % p)