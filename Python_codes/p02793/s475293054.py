
from math import gcd
from functools import reduce


def lcm(x, y):
    return x * y // gcd(x, y)


N = int(input())
X = list(map(int, input().split()))
total = reduce(lcm, X)
MOD = 10 ** 9 + 7

ans = 0
for v in X:
    ans += total * pow(v, MOD - 2, MOD) % MOD
    ans %= MOD

print(ans)
