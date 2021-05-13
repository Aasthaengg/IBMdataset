from collections import Counter
def sieve_eratosthenes(n):
    primes = [0, 1] * (n // 2 + 1)                  # 素数候補の配列。　0: 素数でない 1:素数である　　偶数は素数ではないので、初めから0としている。
    if n % 2 == 0:                                  # 上記の配列が 0 ~ n+1 になってるので一個除く、ただし n が奇数の場合は n+1 は自動的に除かれてるので放置
        primes.pop()
    primes[1] = 0                                   # 1 は素数ではない
    primes[2] = 1                                   # 2 は偶数だけど素数
    for p in range(3, int(n**0.5) + 2, 2):
        if primes[p]:
            for q in range(p * p, n + 1, 2 * p):    # p(p + 2k) k = 1,... と書ける物を素数候補から省く。　2k としているのは、奇数＋奇数の場合を考える必要はないため
                primes[q] = 0
    return primes

N = int(input())
M = 10**4
prime = sieve_eratosthenes(M)
P = []
for i in range(M):
    if prime[i]:
        if i%5==1:
            P.append(i)
print(*P[:N])


