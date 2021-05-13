#!/usr/bin/env python
n = int(input())
ans = 0 

is_primes = [True for _ in range(n+1)]
is_primes[0] = is_primes[1] = False
minFactor = [-1 for _ in range(n+1)]

for i in range(2, n+1):
    if not is_primes[i]: continue
    minFactor[i] = i 
    for j in range(i*i, n+1, i): 
        is_primes[j] = False
        minFactor[j] = i 


def fast_factorization(n):
    data = {}
    while n > 1:
        if minFactor[n] not in data:
            data[minFactor[n]] = 1 
        else:
            data[minFactor[n]] += 1
        n //= minFactor[n]
    return data


def count_divisors(n):
    ret = 1 
    for v in fast_factorization(n).values():
        ret *= (v+1)
    return ret 

for i in range(1, n): 
    ans += count_divisors(i)

print(ans)
