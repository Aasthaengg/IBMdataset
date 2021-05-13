import sys
import numpy as np
input = sys.stdin.buffer.readline
Q = int(input())


def is_prime(v):
    for i in range(2, v):
        if i * i > v:
            break
        if v % i == 0:
            return False
    return True


def make_prime(U):
    is_prime = np.zeros(U, np.bool)
    is_prime[2] = 1
    is_prime[3::2] = 1
    M = int(U**.5) + 1
    for p in range(3, M, 2):
        if is_prime[p]:
            is_prime[p * p::p + p] = 0
    return is_prime


is_primes = make_prime(10**5 + 2)
# print('is_primes', is_primes[:14])

V = [0] * (10**5 + 2)
for i in range(1, len(V)):
    if i % 2 == 0:
        V[i] = V[i - 1]
        continue
    if is_primes[i] and is_primes[(i + 1) // 2]:
        V[i] = V[i - 1] + 1
    else:
        V[i] = V[i - 1]
# print('V', V)

for _ in range(Q):
    l, r = map(int, input().split())
    # print('l - 1, r, V[l- 1], V[r]', l - 1, r, V[l - 1], V[r])
    print(V[r] - V[l - 1])
