n = int(input())

x = 1
for i in range(1, n+1):
    x *= i

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

import collections
c = collections.Counter(prime_factorize(x))
y = list(c.values())

z = 1
for j in range(len(y)):
    z *= (y[j]+1)

print(z % (10**9+7))