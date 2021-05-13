from collections import Counter
N = int(input())
mod = 10 ** 9 + 7

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

primes = []
for i in range(1, N + 1):
    primes += prime_factorize(i)

ans = 1
for v in Counter(primes).values():
    ans *= (v + 1)
    ans %= mod
print(ans)