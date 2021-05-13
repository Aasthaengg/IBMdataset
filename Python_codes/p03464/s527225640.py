import math
import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

K = int(sys.stdin.buffer.readline())
A = list(map(int, sys.stdin.buffer.readline().split()))


def solve():
    if A[-1] == 1:
        lo = 2
        hi = 2
    elif A[-1] == 2:
        lo = 2
        hi = 3
    else:
        return None

    for a in reversed(A[:-1]):
        l = math.ceil(lo / a) * a
        h = math.floor(hi / a) * a
        if not lo <= l <= hi or not lo <= h <= hi:
            return None
        lo = l
        hi = h + a - 1
    return lo, hi


ans = solve()
if ans:
    print(*ans)
else:
    print(-1)
