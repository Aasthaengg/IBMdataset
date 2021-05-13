import sys
import bisect
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
bl = bisect.bisect_left

A, B, Q = map(int, input().split())
inf = 10**18
S = [-inf]+[int(input()) for _ in range(A)]+[inf]
T = [-inf]+[int(input()) for _ in range(B)]+[inf]


def path(x):
    sl = S[bl(S, x) - 1]
    sr = S[bl(S, x)]
    tl = T[bl(T, x) - 1]
    tr = T[bl(T, x)]

    res = 10 ** 18
    res = min(res, abs(x - sl) + abs(sl - tl))
    res = min(res, abs(x - sl) + abs(sl - tr))
    res = min(res, abs(x - sr) + abs(sr - tr))
    res = min(res, abs(x - sr) + abs(sr - tl))
    res = min(res, abs(x - tr) + abs(tr - sl))
    res = min(res, abs(x - tr) + abs(tr - sr))
    res = min(res, abs(x - tl) + abs(tl - sl))
    res = min(res, abs(x - tl) + abs(tl - sr))
    return res


X = [int(input()) for _ in range(Q)]
for x in X:
    print(path(x))