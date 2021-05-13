primes = [2]

def is_prime(num):
    root = num ** 0.5
    for prime in primes:
        if root < prime:
            break
        if num % prime == 0:
            return 0
    return 1

def create_primes(primes, max):
    for i in range(primes[-1] + 1,max):
        if is_prime(i):
            primes += [i]

count = 0
n = int(input())
s = [int(input()) for _ in range(n)]

create_primes(primes, int(max(s) ** 0.5))

print(sum(is_prime(i) for i in s))