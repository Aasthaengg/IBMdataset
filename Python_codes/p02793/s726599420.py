from collections import defaultdict


def prime_factor(n):
    d = defaultdict(int)
    for i in range(2, n + 1):
        if i * i > n:
            break

        while n % i == 0:
            d[i] += 1
            n //= i

    if n != 1:
        d[n] += 1

    return d


N = int(input())
X = list(map(int, input().split()))
MOD = 10 ** 9 + 7

ctr = defaultdict(int)
buf = []
for n in X:
    d = prime_factor(n)
    buf.append(d)
    for key in d:
        ctr[key] = max(ctr[key], d[key])

total = 1
for key, val in ctr.items():
    total *= pow(key, val, MOD)
    total %= MOD

ans = 0
for i, n in enumerate(X):
    cur = total
    for key, val in buf[i].items():
        cur = cur * pow(pow(key, val, MOD), MOD - 2, MOD) % MOD

    ans += cur
    ans %= MOD

print(ans)
