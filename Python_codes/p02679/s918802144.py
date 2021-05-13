from collections import defaultdict
from math import gcd
N = int(input())
d = defaultdict(int)
s = set()
ans = 0
mod = 1000000007

def change(A, B):
    if A == 0 and B == 0:
        return (0, 0)
    if A == 0:
        return (0, 1)
    if B == 0:
        return (1, 0)
    GCD = gcd(A, B)
    A //= GCD
    B //= GCD
    if A < 0:
        A *= -1
        B *= -1
    return (A, B)

def pair(key):
    if key == (1, 0):
        return (0, 1)
    A, B = key
    return (B, -A)

for i in range(N):
    A, B = map(int,input().split())
    A, B = change(A, B)
    if A == 0 and B == 0:
        ans += 1
    else:
        d[(A, B)] += 1
        if A == 0:
            A, B = B, A
        elif B < 0:
            A, B = -B, A
        s.add((A, B))

cnt = 1
for k in s:
    cnt *= pow(2, d[k], mod) + pow(2, d[pair(k)], mod) - 1
    cnt %= mod
cnt -= 1
ans += cnt
ans %= mod

print(ans)