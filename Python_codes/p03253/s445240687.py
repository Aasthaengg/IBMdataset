import sys
from collections import defaultdict
import math
input = sys.stdin.readline
N, M = [int(x) for x in input().strip().split()]
d = defaultdict(int)
M_ = M
MOD = 10 ** 9 + 7

if M == 1:
    print(1)
    exit()

while True:
    for i in range(2, int(M_ ** 0.5) + 1):
        if M_ % i == 0:
            M_ //= i
            d[i] += 1
            break
    else:
        if M_ != 1:
            d[M_] += 1
        break

maxi = max(d.values())
fact = [0] * (maxi + N + 1)
p = 1

def nCr(n, r):
    if r > n - r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n

    ret = 1
    for i in range(1, r+1):
        ret *= (n-(i-1))
        ret //= i

    return ret

ans = 1
nCr_d = {}
for key, val in d.items():
    if (val+N-1, N-1) not in nCr_d:
        nCr_d[(val+N-1, N-1)] = nCr(val+N-1, N-1)
    ans = (ans * nCr_d[(val+N-1, N-1)]) % MOD

print(ans)