import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from math import gcd
from collections import Counter
from fractions import Fraction

def resolve():
    n = int(input())
    zero = 0
    counter = Counter()
    for _ in range(n):
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            zero += 1
            continue

        g = gcd(x, y)
        x //= g
        y //= g

        if x == 0:
            x, y = 0, 1
        elif x < 0:
            x, y = -x, -y
        counter[x, y] += 1

    C = list(counter.items())
    C.sort(key = lambda p: Fraction(p[0][1], p[0][0]) if p[0][0] != 0 else -float("inf"))

    k = len(C)
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(k):
        x, y = C[i][0]
        dp[i + 1] += dp[i]
        dp[i + 1] += (pow(2, counter[x, y], MOD) - 1) * dp[i] * pow(2, -counter[y, -x] % (MOD - 1), MOD)
        dp[i + 1] %= MOD

    res = dp[k]
    res -= 1
    res += zero
    print(res % MOD)
resolve()