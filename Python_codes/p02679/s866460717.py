import sys
from collections import Counter
from math import gcd

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

N = INT()
C = Counter()
zero = 0
for i in range(N):
    a, b = MAP()
    if a == b == 0:
        zero += 1
    elif a == 0:
        C[(0, 1, 0)] += 1
    elif b == 0:
        C[(1, 0, 1)] += 1
    else:
        g = gcd(a, b)
        ga, gb = a // g, b // g
        C[((a < 0) ^ (b < 0), abs(ga), abs(gb))] += 1

ans = 1
for k, v in C.items():
    if v == 0:
        continue
    op, a, b = k
    ans *= pow(2, C[(op, a, b)], MOD) + pow(2, C[(1-op, b, a)], MOD) - 1
    ans %= MOD
    if (1-op, b, a) in C:
        C[(1-op, b, a)] = 0
print((zero+ans-1)%MOD)
