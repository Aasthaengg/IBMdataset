import math
import functools
import sys

N = int(input())
A = list(map(int, input().split()))

wise = functools.reduce(math.gcd, A)
if wise != 1:
    print('not coprime')
    sys.exit(0)

A = list(filter(lambda a: a != 1, A))

if len(A) == 0:
    print('pairwise coprime')
    sys.exit(0)

pcount = 78498
if len(A) > pcount:
    print('setwise coprime')
    sys.exit(0)

Amax = max(A) + 1

hurui = [1] * 1001
primes = []

for n in range(2, 1001):
    if hurui[n] != 1:
        continue

    primes.append(n)

    k = 2
    while n * k <= 1000:
        hurui[n * k] = n
        k += 1




count = [0] * (Amax+1)

pairwise = True
for i in range(len(A)):
    a = A[i]
    if a == 1:
        continue

    for p in primes:
        if a % p == 0:
            count[p] += 1
            while a % p == 0:
                a = a // p
    if a != 1:
        count[a] += 1

if max(count)==1:
    print('pairwise coprime')
else:
    print('setwise coprime')
