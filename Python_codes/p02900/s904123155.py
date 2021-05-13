from collections import Counter
def prime_factorize(n):
    f = 2
    primes = []
    while f * f <= n:
        if n % f != 0:
            f += 1
            continue
        primes.append(f)
        n //= f
    if n > 1:
        primes.append(n)
    return list(set(primes))
a, b = map(int, input().split())
ab_primes = Counter(prime_factorize(a) + prime_factorize(b))
ans = 0
for prime in ab_primes.values():
    if prime > 1:
        ans += 1
print(1 + ans)