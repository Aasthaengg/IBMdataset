from math import sqrt


def sieve(x):
    """
    Sieve of Eratosthenes
    :param x: max value
    :return: list of primes
    """

    primes = []
    li = list(range(2, x + 1))

    while li[0] <= sqrt(x):
        p = li[0]
        primes.append(p)
        li = [e for e in li if e % p != 0]

    primes += li
    return primes


n = int(input())

primes = sieve(55555)
mod5is1 = [e for e in primes if e % 5 == 1]
ans = mod5is1[:n]
print(*ans)
