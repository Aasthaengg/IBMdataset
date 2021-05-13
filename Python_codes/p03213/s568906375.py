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

primes = primes(100)

N = int(input())

# e[i]: N!の素因数分解でのiの指数
e = [0] * (N+1)
for i in range(2,N+1):
    cur = i
    for p in primes:
        while cur % p == 0:
            e[p] += 1
            cur //= p

# eの要素で(M - 1)以上のものの個数
cnt = lambda M: len(tuple(filter(lambda x: x >= M - 1, e)))

ans = cnt(75) # 75
ans += cnt(25) * (cnt(3) - 1) # 25 * 3 = 75
ans += cnt(15) * (cnt(5) - 1) # 15 * 5 = 75
# 「// 2」は2つのcnt(5)は区別しないから
ans += cnt(5) * (cnt(5) - 1) * (cnt(3) - 2) // 2 # 5 * 5 * 3 = 75

print(ans)