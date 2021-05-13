def factorization(n):
    ans = {}
    i = 2
    while n > 1:
        count = 0
        while n % i == 0:
            n = n // i
            count += 1
        if count != 0:
            ans[i] = count
        i += 1
    return ans


N = int(input())
primes = {}
for n in range(2, N + 1):
    factors = factorization(n)
    for f in factors:
        if f in primes:
            primes[f] += factors[f]
        else:
            primes[f] = factors[f]

ans = 0
# 75
for p in primes:
    if primes[p] >= 74:
        ans += 1

# 25 * 3 and 15 * 5
for p in primes:
    for q in primes:
        if p == q:
            continue
        if primes[p] >= 24 and primes[q] >= 2:
            ans += 1
        if primes[p] >= 14 and primes[q] >= 4:
            ans += 1

# 3 5 5
for p in primes:
    if primes[p] >= 2:
        for q in primes:
            if p != q and primes[q] >= 4:
                for r in primes:
                    if p != r and q != r and primes[r] >= 4 and q < r:
                        ans += 1
print(ans)