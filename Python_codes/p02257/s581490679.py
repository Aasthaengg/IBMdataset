#!/usr/bin/env python3
from itertools import takewhile
from math import sqrt


def is_prime(primes, i):
    if i in primes:
        return True
    for p in takewhile(lambda x: x * x <= i, sorted(primes)):
        if i % p == 0:
            return False
    return True


def sieve_of_eratosthenes(max):
    is_prime = [True] * (max + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(sqrt(max)) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * i, max + 1, i):
            is_prime[j] = False
    return filter(lambda x: is_prime[x], range(max + 1))

primes = set(sieve_of_eratosthenes(10000))

n = int(input())
c = 0
for _ in range(n):
    i = int(input())
    if is_prime(primes, i):
        c += 1
print(c)