#!/usr/bin/env python
import math

n = int(input())
A = list(map(int, input().split()))

is_prime = [True for _ in range(1100000)]
is_prime[0] = is_prime[1] = False

for i in range(2, 1100000):
    if not is_prime[i]: continue
    for j in range(i*i, 1100000, i): 
        is_prime[j] = False 

g = 0 
for a in A:
    g = math.gcd(g, a)

if g != 1:
    print('not coprime')
    exit()

used = [False for _ in range(1100000)]
primes = [a for a in A if is_prime[a]]
not_primes = [a for a in A if not is_prime[a]]

for p in primes:
    used[p] = True

small_prime = [p for p in range(1100) if is_prime[p]]
for a in not_primes:
    for p in small_prime:
        if a == 1: break
        if a%p != 0: continue
        if used[p]:
            print('setwise coprime')
            exit()
        used[p] = True
        while a%p == 0:
            a //= p
    if a > 1:
        if used[a]:
            print('setwise coprime')
            exit()
        used[a] = True

print('pairwise coprime')
