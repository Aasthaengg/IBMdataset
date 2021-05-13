import numpy as np

n = int(input())
a = np.array(input().split(), dtype=int)

ans = 0
MOD = 10**9+7

k = max(a)
j = 0
while k:
    bits = (a>>j)&1
    one = np.count_nonzero(bits)
    ans += (one%MOD)*((n-one)%MOD)*pow(2,j,MOD)
    ans %= MOD
    j += 1
    k >>= 1

print(ans)