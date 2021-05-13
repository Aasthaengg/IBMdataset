import sys
from collections import Counter

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M = lr()
MOD = 10 ** 9 + 7

def prime_factorize(n): # Nの素因数分解
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

def combination(n, x, mod=10**9+7):
    # nCx 組み合わせ ex) combination(5, 2) = 10
    factorial = [1] * (n+1)
    t = 1
    for i in range(1, n+1):
        t = (t * i) % mod
        factorial[i] = t
    tmp = factorial[n]
    tmp = (tmp * pow(factorial[x], mod-2, mod)) % mod
    tmp = (tmp * pow(factorial[n-x], mod-2, mod)) % mod
    return tmp

A = prime_factorize(M)
counter = Counter(A)
answer = 1
for c in counter.values():
    answer *= combination((N-1+c), c)
    answer %= MOD

print(answer)
# 19