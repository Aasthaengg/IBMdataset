N = int(input())
if N == 1:
    print(1)
    exit()
# calculate primes by sieve
primes = list(range(2, N + 1))
prime_index = 0
n = primes[prime_index]
while n**2 <= N:
    primes = list(filter(lambda x: x == n or x % n != 0, primes))
    prime_index += 1
    n = primes[prime_index]
# calculate exponents
exponents = [0 for _ in range(len(primes))]
for n in range(2, N + 1):
    for prime_index, prime in enumerate(primes):
        exponent = 0
        tmp = n
        while tmp % prime == 0:
            tmp //= prime
            exponent += 1
        exponents[prime_index] += exponent
# calculate answer
const = 10**9 + 7
answer = 1
for e in exponents:
    answer = answer * (e + 1)
    answer %= const
print(answer)