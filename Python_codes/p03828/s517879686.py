MOD = 10 ** 9 + 7
n = int(input())

# 素数
primes = [True] * (n + 1)
p = 2
while p * p <= n:
    if primes[p]:
        for i in range(p * p, n + 1, p):
            primes[i] = False
    p += 1
primes[0], primes[1] = False, False

# counter
cnt = [0] * (n + 1)
for k in range(2, n + 1):
    now = k
    # 素因数分解
    for i in range(2, k + 1):
        while k % i == 0:
            cnt[i] += 1
            k //= i
    if k != 1:
        cnt[k] += 1

res = 1
for k in range(1, n + 1):
    if primes[k]:
        res *= cnt[k] + 1
        res %= MOD

print(res)