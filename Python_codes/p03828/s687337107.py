from collections import Counter


def prime_factorization(n):
    """
    nを素因数分解して素因数のリストを返却する
    """
    if n < 2:
        return [n]

    primes = []
    while n % 2 == 0:
        primes.append(2)
        n //= 2
    i = 3
    while i ** 2 <= n:
        while n % i == 0:
            primes.append(i)
            n //= i
        i += 2
    if n != 1:
        primes.append(n)
    return primes


MOD = 10 ** 9 + 7
N = int(input())

counter = Counter()

for n in range(2, N + 1):
    for p in prime_factorization(n):
        counter[p] += 1

ans = 1
for k, v in counter.items():
    if k < 2:
        continue
    ans *= v + 1
    ans %= MOD

print(ans)
