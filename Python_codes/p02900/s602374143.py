
from collections import defaultdict


def prime_factor(n):
    d = defaultdict(int)
    for i in range(2, n + 1):
        if i * i > n:
            break

        while n % i == 0:
            d[i] += 1
            n //= i

    if n != 1:
        d[n] += 1

    return d


A, B = map(int, input().split())
prime_a = prime_factor(A)
prime_b = prime_factor(B)
print(len(set(prime_a) & set(prime_b)) + 1)
