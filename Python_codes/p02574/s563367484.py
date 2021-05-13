from functools import reduce
from math import gcd
def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    M = max(A)

    if reduce(gcd, A) != 1:
        print("not coprime")
        return

    # linear sieve
    sieve = list(range(M + 1))
    primes = []
    for i in range(2, M + 1):
        if sieve[i] == i:
            primes.append(i)
        for p in primes:
            if sieve[i] < p or i * p > M:
                break
            sieve[i * p] = p

    # prime factorization
    used = [False] * (M + 1)
    for a in A:
        primes = set()
        while a != 1:
            p = sieve[a]
            primes.add(p)
            a //= p
        for p in primes:
            if used[p]:
                print("setwise coprime")
                return
            used[p] = True
    print("pairwise coprime")
resolve()