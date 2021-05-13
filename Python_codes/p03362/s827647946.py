N = int(input())


def eratosthenes_sieve(n):
    if n < 2:
        return []

    is_primes = [True] * (n + 1)
    for x in range(2, int(n ** 0.5 + 1) + 1):
        if is_primes[x]:
            for mx in range(2 * x, n + 1, x):
                is_primes[mx] = False

    return [i for i in range(2, n + 1) if is_primes[i]]


P = eratosthenes_sieve(55555)
P = [p for p in P if p % 5 == 1]
print(' '.join(map(str, P[:N])))
