# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# lcm、逆元
MOD = 10 ** 9 + 7

N = ir()
A = np.array(lr())

U = 10 ** 6 + 10
is_prime = np.zeros(U, np.bool)
is_prime[2] = 1
is_prime[3::2] = 1
for p in range(3, U, 2):
    if p*p > U:
        break
    if is_prime[p]:
        is_prime[p*p::p+p] = 0

M = 10 ** 3
small_primes = np.where(is_prime[:M])[0].tolist()

B = A.copy()
lcm = 1
for p in small_primes:
    e = 0
    while np.any(A%p == 0):
        e += 1
        A[A%p == 0] //= p
    lcm *= p ** e
    lcm %= MOD

for p in set(A.tolist()):
    lcm *= p
    lcm %= MOD

B = sum(pow(x, MOD-2, MOD) for x in B.tolist()) % MOD
B *= lcm
answer = B % MOD
print(answer % MOD)
# np.int64とint型の違いに注意