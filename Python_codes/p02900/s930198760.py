from functools import lru_cache


@lru_cache(maxsize=None)
def prime_factorization(n):
    """
    nを素因数分解して素因数のリストを返却する
    """
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n //= 2
    i = 3
    while i ** 2 <= n:
        while n % i == 0:
            primes.append(i)
            n //= i
        i += 2
    if n != 1:
        primes.append(n)
    return primes


A, B = map(int, input().split(' '))

a_primes = set(prime_factorization(A))
b_primes = set(prime_factorization(B))

print(len(a_primes & b_primes) + 1)
