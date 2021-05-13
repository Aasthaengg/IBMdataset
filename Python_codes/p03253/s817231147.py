from collections import Counter

n, m = map(int, input().split())
MOD = 10 ** 9 + 7
SIZE = 10 ** 5 * 2
fact = [0] * SIZE
inv = [0] * SIZE
finv = [0] * SIZE
fact[0], fact[1] = 1, 1
inv[1] = 1
finv[0], finv[1] = 1, 1
for i in range(2, SIZE):
    fact[i] = fact[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD


def modcomb(n, r):
    if n < 0 or r < 0 or n < r:
        return 0
    return fact[n] * (finv[r] * finv[n - r] % MOD) % MOD


def prime_factorize(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            res.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        res.append(n)
    return res


counter = Counter(prime_factorize(m))
ans = 1
for v in counter.values():
    ans *= modcomb(v + n - 1, n - 1)
    ans %= MOD
print(ans)
