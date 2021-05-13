N, M = map(int, input().split())
S = input()
T = input()

import sys

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b%a, a)


g = gcd(N, M)
sn = N//g
sm = M//g

ok = True
for k in range(0, g):
    a = k * sn
    b = k * sm
    if S[a] != T[b]:
        ok = False
        break

if ok:
    print(N*M//g)
else:
    print(-1)