import math
from collections import Counter

n, m = map(int, input().split())
mod = 10**9 + 7

K = 50
fact = [0] * (n+1+K)
ifact = [0] * (n+1+K)
fact[0] = 1
for i in range(1,n+1+K):
    fact[i] = fact[i-1] * i % mod
ifact[n+K] = pow(fact[n+K], mod-2, mod)
for i in reversed(range(1,n+1+K)):
    ifact[i-1] = ifact[i] * i % mod

def comb(n, k):
    return fact[n] * ifact[n-k] % mod * ifact[k] % mod

def getprime(n):
    primes = []
    i = 2
    while n >= i * i:
        while n % i == 0:
            n //= i
            primes.append(i)
        i += 1
    if n != 1:
        primes.append(n)
    return primes

ans = 1
counter = Counter(getprime(m))
for k in counter.values():
    ans *= comb(n+k-1, k)
    ans %= mod
print(ans)