import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from math import gcd
from collections import Counter
from functools import cmp_to_key

def cmp(A1, A2):
    x1, y1 = A1[0]
    x2, y2 = A2[0]
    if (x1, y1) == (x2, y2):
        return 0
    return -1 if x2 * y1 < x1 * y2 else 1

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

        if y == 0:
            x, y = 1, 0
        elif y < 0:
            x, y = -x, -y
        counter[x, y] += 1

    C = list(counter.items())
    C.sort(cmp_to_key(cmp))

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