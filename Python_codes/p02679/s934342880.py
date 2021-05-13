from collections import defaultdict
from math import gcd
import sys


MOD = 10 ** 9 + 7
N = int(input())
sar = defaultdict(int)
zero = 0
for s in sys.stdin.readlines():
    A, B = map(int, s.split())
    if (A, B) == (0, 0):
        zero += 1
    else:
        a = abs(A)
        b = abs(B)
        x = gcd(a, b)
        if a == 0:
            sar[(0, b // x, 1)] += 1
        elif b == 0:
            sar[(a // x, 0, 0)] += 1
        else:
            sar[(a // x, b // x, int((A >= 0) ^ (B >= 0)))] += 1

ans = 1
done = set()
for k in list(sar.keys()):
    a, b, c = k
    if (a, b, c) not in done:
        cnt = pow(2, sar[(a, b, c)], MOD) + pow(2, sar[(b, a, c ^ 1)], MOD) - 1
        ans *= cnt
        ans %= MOD
        done.add((a, b, c))
        done.add((b, a, c ^ 1))

ans -= 1
ans += zero

print(ans % MOD)
