# -*- coding: utf-8 -*-
from math import sqrt
from bisect import bisect

def inpl(): return tuple(map(int, input().split()))

def isprime(N, P):
    if N <= 1:
        return False
    for p in P[:bisect(P, sqrt(N))]:
        if N%p==0:
            return False
            break
    else:
        return True

def primes(N):
    P = [2]
    searched = [False]*(N+1)
    for i in range(3, N+1, 2):
        if searched[i]:
            continue
        P.append(i)
        for j in range(i, N+1, i):
            searched[j] = True
    return P

P = primes(int(sqrt(10**8)))

res = 0
for i in range(int(input())):
    res += isprime(int(input()), P)
print(res)
