from itertools import accumulate
Q = int(input())
m = 0
ls = []
for i in range(Q):
    l, r = map(int, input().split())
    m = max(m, max(l, r))
    ls.append((l, r))

def sieve_eratosthenes(n):
    primes = [0, 1] * (n // 2 + 1)
    if n % 2 == 0:
        primes.pop()
    primes[1] = 0
    primes[2] = 1
    for p in range(3, n + 1, 2):
        if primes[p]:
            for q in range(p * p, n + 1, 2 * p):
                primes[q] = 0
    return primes

a = sieve_eratosthenes(m)
b = [0 for i in range(m+1)]
for i in range(2, m+1):
    if i%2 == 1 and a[i] == 1 and a[(i+1)//2] == 1:
        b[i] = 1
c = list(accumulate(b))
for l, r in ls:
    print(c[r] - c[l-1])
