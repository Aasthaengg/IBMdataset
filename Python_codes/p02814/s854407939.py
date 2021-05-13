
from math import gcd
from functools import reduce


def lcm(x, y):
    return x * y // gcd(x, y)


def count_2p(n):
    res = 0
    while n % 2 == 0:
        res += 1
        n //= 2
    return res


N, M = map(int, input().split())
X = list(map(int, input().split()))

p2_cnt = [count_2p(n) for n in X]
if all(p2_cnt[0] == p2_cnt[i] for i in range(N)):
    a = reduce(lcm, X)
    cnt = M // (a // 2)
    print(-(-cnt // 2))
else:
    print(0)
