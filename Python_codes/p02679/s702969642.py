import math
import sys
from collections import defaultdict

input = sys.stdin.readline
mod = 1000000007

n = int(input())

n2 = [1]
for _ in range(n):
    n2.append(n2[-1] * 2 % mod)

zero = 0
plus = defaultdict(int)
minus = defaultdict(int)

for _ in range(n):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        zero += 1
        continue
    elif a == 0:
        plus[(1, 0)] += 1
    elif b == 0:
        minus[(1, 0)] += 1
    else:
        p = math.gcd(a, b)
        a //= p
        b //= p
        if a * b > 0:
            plus[(abs(a), abs(b))] += 1
        else:
            minus[(abs(b), abs(a))] += 1

n -= zero
ans = 1

for k, v in plus.items():
    if minus[k] > 0:
        ans *= (n2[v] + n2[minus[k]] - 1)
        ans %= mod
        n -= v + minus[k]

ans *= n2[n]
ans %= mod
ans += zero - 1
ans %= mod
print(ans)
