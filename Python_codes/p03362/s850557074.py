import math


def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


N = int(input())
primes = get_sieve_of_eratosthenes(55555)
#print(len(primes))
#print(primes)
primes = [x for x in primes if x % 5 == 1]
print(*primes[:N])