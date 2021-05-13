import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

from functools import lru_cache

def F(N):
    if N < 10:
        return N
    q, r = divmod(N, 10)
    x1 = F(q) + r
    x2 = F(q-1) + 9
    return max(x1, x2)
ans = F(int(input()))
print(ans)