from itertools import combinations
n = int(input())
primes = []
for num in range(2, 55556):
    for prime in primes:
        if num % prime == 0:
            break
    else:
        primes.append(num)

primes_mod1 = []
for prime in primes:
    if prime % 5 == 1:
        primes_mod1.append(prime)
print(*primes_mod1[:n], sep=" ")