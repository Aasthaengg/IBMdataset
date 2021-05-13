# https://atcoder.jp/contests/abc096/tasks/abc096_d

N = int(input())

# 最大55,555以下の素数
MAX_N = 55556
primes = [True] * MAX_N
primes[0] = primes[1] = False
for p in range(2, MAX_N):
    if not primes[p]:
        continue
    for m in range(2 * p, MAX_N, p):
        primes[m] = False
lps = [i for i in range(2, MAX_N) if primes[i] and i % 5 == 1]

ans = lps[:N]
print(*ans)