from fractions import gcd
from functools import reduce

N, M = map(int,input().split())
a = list(map(int,input().split()))
a = [x // 2 for x in a]

def solve(p, q):
    g = gcd(p, q)
    p //= g
    q //= g
    if (p - q) % 2 == 1:
        return 0
    return p * q * g

k = reduce(solve, a)
if k == 0:
    print(0)
else:
    print(M // k - M // (k * 2))