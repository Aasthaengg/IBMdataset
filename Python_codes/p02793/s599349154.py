from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

primes_total = defaultdict(int)

for a in A:
    tmp = a
    primes_a = defaultdict(int)
    p = 2
    while p * p <= tmp:
        while tmp % p == 0:
            primes_a[p] += 1
            tmp //= p
        p += 1
    if tmp != 1:
        primes_a[tmp] += 1

    for k in primes_a.keys():
        primes_total[k] = max(primes_total[k], primes_a[k])

lcm = 1
for k in primes_total.keys():
    lcm *= pow(k, primes_total[k], MOD)
    lcm %= MOD

ans = 0

for a in A:
    # フェルマーの小定理より
    ans += lcm * pow(a, MOD - 2, MOD)
    ans %= MOD

print(ans)