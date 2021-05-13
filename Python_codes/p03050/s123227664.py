from collections import Counter
from itertools import product

from functools import reduce
import operator
int_product = lambda it: reduce(operator.mul,it,1)

# 素因数分解
def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            yield i
    if n > 1:
        yield n

def divisors(n):
    factors = prime_factors(n)
    factors = Counter(factors)
    pows = tuple(factors.values())
    factors = tuple(factors.keys())
    for pp in product(*(range(p+1) for p in pows)):
        yield int_product(f**p for f,p in zip(factors,pp))


N = int(input())
res = 0
for d in divisors(N):
    m = d-1
    if m > 0 and N//m == N%m:
        res += m

print(res)