from math import sqrt
from scipy.misc import comb

n, m = map(int, input().split())
mod = 10 ** 9 + 7


def sieve(x):
    primes = []
    li = list(range(2, x + 1))

    while li[0] <= sqrt(x):
        p = li[0]
        primes.append(p)
        li = [e for e in li if e % p != 0]

    primes += li
    return primes


def prime_fact(x):
    primes = sieve(int(sqrt(x)) + 1)
    d = {}

    for p in primes:
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1

        if cnt:
            d[p] = cnt

    if x != 1:
        d[x] = 1

    return d


pf = prime_fact(m)
ans = 1
for v in pf.values():
    ans *= comb(v + n - 1, v, exact=True)
    ans %= mod

print(ans)
