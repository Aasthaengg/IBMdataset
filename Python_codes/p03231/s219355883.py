import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from math import gcd
def resolve():
    fixed = {}
    n, m = map(int, input().split())
    S = input()
    T = input()
    l = n // gcd(n, m) * m
    for i in range(n):
        fixed[i * l // n] = S[i]
    for j in range(m):
        if not j * l // m in fixed:
            continue
        if fixed[j * l // m] != T[j]:
            print(-1)
            return
    print(l)
resolve()