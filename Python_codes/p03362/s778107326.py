from math import factorial

k = int(input())
n = 10000
primes = [2]
for i in range(3, n, 2):
    all(i % p != 0 for p in primes) and primes.append(i)

primes = [i for i in primes if i%5 == 1][:k]
print(*primes)