n = 10**5 + 3
primes = set(range(3, n+1, 2))

for i in range(3, int(n**0.5+1)):
    primes.difference_update(range(i*2, n+1, i))
primes.add(2)
primes = list(primes)
primes.sort()

x = int(input())

primes = [y for y in primes if y >= x]

print(primes[0])