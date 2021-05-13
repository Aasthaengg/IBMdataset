# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

U = 55555
is_prime = np.zeros(U, np.bool)
is_prime[2] = 1
is_prime[3::2] = 1
for p in range(3, U, 2):
    if p*p > U:
        break
    if is_prime[p]:
        is_prime[p*p::p+p] = 0

primes = np.where(is_prime)[0]
primes = primes[primes%5 == 2]
N = ir()
answer = primes[:N]
print(*answer)
