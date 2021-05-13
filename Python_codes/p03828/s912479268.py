import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9 + 7

def prime_factorize(n):
    prime_fact = []
    while n%2 == 0:
        prime_fact.append(2)
        n//=2
    f = 3
    while f * f <= n:
        if n % f == 0:
            prime_fact.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        prime_fact.append(n)
    return prime_fact

n = int(input())
a = 1
ans = 0
for i in range(1,n+1):
    a *= i
c = prime_factorize(a)
d = collections.Counter(c)
ans = 1
for value in d.values():
    ans *= (value+1)
    ans %= MOD
print(ans)