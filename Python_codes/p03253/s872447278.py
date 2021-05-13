from collections import Counter
from math import factorial
n, m = map(int, input().split())
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
c = Counter(prime_factorize(m)).values()
def combinations(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))
ans = 1
mod = 10**9 + 7
for i in c:
  ans *= combinations(i+n-1, i)
  ans %= mod
print(ans)