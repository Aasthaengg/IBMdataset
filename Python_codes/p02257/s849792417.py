primes = [2]

def is_prime(num):
    root = num ** 0.5
    for prime in primes:
        if root < prime:
            break
        if num % prime == 0:
            return False
    return True

def create_primes(primes, max):
    for i in range(primes[-1] + 1,max):
        if is_prime(i):
            primes += [i]

create_primes(primes, 10000)

n = int(input())
count = 0
for _ in range(n):
    num = int(input())
    count += 1 if is_prime(num) else 0
print(count)