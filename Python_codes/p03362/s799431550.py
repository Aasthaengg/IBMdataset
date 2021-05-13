import numpy as np
def make_primes(U=55555):
    is_prime = np.zeros(U,np.bool)
    is_prime[2] = 1
    is_prime[3::2] = 1
    M = int(U**.5)+1
    for p in range(3,M,2):
        if is_prime[p]:
            is_prime[p*p::p+p] = 0
    return is_prime.nonzero()[0], is_prime
n = int(input())
a = []
primes, is_prime = make_primes()
for pi in primes:
    if pi % 5 == 1:
        a.append(pi)

print(' '.join(map(str, a[:n])))
