from collections import defaultdict
from math import gcd

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
mod = 10 ** 9 + 7
MAX = 2 * 10 ** 5

p = defaultdict(int)
m = defaultdict(int)
ab0 = 0
for a, b in ab:
    if a == 0 and b == 0:
        ab0 += 1

    elif a == 0:
        m[(0, 1)] += 1
        p[(1, 0)]

    elif b == 0:
        p[(1, 0)] += 1

    else:
        g = gcd(a, b)
        a //= g
        b //= g
        sign = a * b
        a = abs(a)
        b = abs(b)
        if sign < 0:
            m[(a, b)] += 1
            p[(b, a)]
        else:
            p[(a, b)] += 1

power = [1]
for _ in range(MAX):
    power.append(power[-1] * 2 % mod)

ans = 1
for (a, b), v in p.items():
    ans *= power[v] + power[m[(b, a)]] - 1
    ans %= mod

ans -= 1
ans += ab0
ans %= mod
print(ans)
