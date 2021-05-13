def comb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)
import math

MOD = 10 ** 9 + 7
N, K = map(int, input().split())
ans = 0
for j in range(K):
    if N-K - j < 0:
        print(0)
        continue
    tmp = (comb(N-K+1, j+1)) % MOD
    print(int((comb(K-1, j) * tmp) % MOD))
