import math
from functools import reduce

N = int(input())
A = list(map(int, input().split()))

max_A = max(A)
sqrt_max_A = math.ceil(max_A ** 0.5)
sieve = list(range(2, max_A+1))
prime = list(range(max_A+1))
while len(sieve) > 0 and sieve[0] <= sqrt_max_A:
    p = sieve[0]
    prime[p]= p
    new_sieve = []
    for s in sieve:
        if s % p == 0:
            prime[s] = p
        else:
            new_sieve.append(s)
    sieve = new_sieve

factors = {}
pairwise = True
for a in A:
    while prime[a] != a:
        if prime[a] in factors:
            pairwise = False
            break
        factors[prime[a]] = True
        p = prime[a]
        while a % p == 0:
            a //= p
    if a != 1:
        if a in factors:
            pairwise = False
        else:
            factors[a] = True
    if not pairwise:
        break
if pairwise:
    print('pairwise coprime')
else:
    gcd = reduce(math.gcd, A)
    if gcd == 1:
        print('setwise coprime')
    else:
        print('not coprime')
