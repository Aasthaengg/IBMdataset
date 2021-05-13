import heapq
from collections import defaultdict, deque
from math import ceil, factorial
from fractions import gcd
import sys
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7

si = lambda: input().strip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
smii = lambda: sorted(map(int, input().split()))


def get_divisor(n):
    divs = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return divs


n = ii()
ans = 0

# K が N の約数のとき
for x in get_divisor(n):
    if x == 1:
        continue
    tmp = n
    while tmp % x == 0:
        tmp //= x
    if tmp % x == 1:
        ans += 1

# K が N の約数でないとき
# 1 は除く
ans += len(get_divisor(n-1)) - 1

print(ans)

