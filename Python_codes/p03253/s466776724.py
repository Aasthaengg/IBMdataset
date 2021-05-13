import collections
import math

N, M = map(int, input().split())


def prime_factorize(n: int) -> list:
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            primes.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        primes.append(n)
    return primes


def comb(n: int, r: int) -> int:
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


if M == 1:
    print(1)
else:
    primes = collections.Counter(prime_factorize(M))
    res = 1
    for freq in primes.values():
        res *= comb(N + freq - 1, freq)
        res %= (10 ** 9 + 7)
    print(res)
