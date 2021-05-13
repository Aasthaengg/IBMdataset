import math
from bisect import bisect_left

X = int(input())

def primes_ref(x):
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0
    x_sqrt = math.sqrt(x)

    for prime in primes:
        if prime == 0: continue 
        if prime > x_sqrt: break
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]

def find_ge(a, x):
  i = bisect_left(a, x)
  if i != len(a):
    return a[i]
  raise ValueError

primes = primes_ref(min(X * X, 100004))
print(find_ge(primes, X))