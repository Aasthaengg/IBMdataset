import sys
input = sys.stdin.readline

N = int(input())

# 素因数分解 (dictバージョン)
# 考え方：1~√nまで実際に割れるか試せば良いが、割れた場合は割れる限りその数で割り続ける
# 計算量：O(√n)
def prime_factorize(n, primes):
    i = 2
    while i * i <= n:
        if n % i != 0:
            i += 1
            continue
        exp = 0
        while n % i == 0:
            exp += 1
            n = n // i
        if i not in primes:
            primes[i] = exp
        else:
            primes[i] += exp
        i += 1
    # 最後に残った数は1か素数にしかならない
    if n != 1:
        if n not in primes:
            primes[n] = 1
        else:
            primes[n] += 1
    return primes


primes = {}
for k in range(1, N+1):
        primes = prime_factorize(k, primes)
count = 1
for p in primes:
    count *= (primes[p] + 1)
ans = count % (10**9 + 7)
print(ans)