from itertools import combinations


def get_primes(N):
    primes = []
    for num in range(2, N + 1):
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.append(num)
    return primes


N = int(input())

primes = get_primes(55555)

# 列挙した素数のうち、5で割った余りが1であるものだけ抽出
primes_5 = []
for prime in primes:
    if prime % 5 == 1:
        primes_5.append(prime)

primes_5 = primes_5[:N]
print(*primes_5)
