def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

N = int(input())

# exp[i]: iの指数
exp = [0] * (N + 1)
primes = primes(N)
for n in range(2, N + 1):
    num = n
    for prime in primes:
        while num % prime == 0:
            exp[prime] += 1
            num //= prime

cnt = lambda X: len([e for e in exp if e >= X])

ans = cnt(74)
ans += cnt(14) * (cnt(4) - 1)
ans += cnt(24) * (cnt(2) - 1)
ans += cnt(4) * (cnt(4) - 1) * (cnt(2) - 2) // 2

print(ans)