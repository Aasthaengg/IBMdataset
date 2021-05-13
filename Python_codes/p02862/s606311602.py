import sys
input = sys.stdin.readline
from collections import defaultdict, deque

(x, y), res, MOD = map(int, input().split()), 0, int(1e9) + 7
if (x + y) % 3 == 0:
    a, b = (y * 2 - x) // 3, (x * 2 - y) // 3
    if all([True if x >= 0 else False for x in (a, b)]):
        l, r = 1, 1
        for i in range(a + 1, a + b + 1): l = (l * i) % MOD
        for i in range(1, b + 1): r = (r * i) % MOD
        res = l * pow(r, MOD - 2, MOD)
print(res % MOD)