#!/usr/bin/env python3
def primes(n):
    m = 1303
    is_prime = [True] * (m + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(m**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, m + 1, i):
            is_prime[j] = False
    return [i for i in range(m + 1)
            if is_prime[i] and str(i).endswith("3")][:n]


print(*primes(int(input())))
