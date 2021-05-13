import collections
import math

N = int(input())
N = math.factorial(N)
INF = 10 ** 9 + 7

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

res = collections.Counter(prime_factorize(N))
keys = list(res.keys())
length = len(keys)
ans = 1
for i in range(length):
    ans = (ans * (res[keys[i]] + 1)) % INF
print(ans)