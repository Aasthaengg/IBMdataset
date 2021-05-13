from bisect import bisect_left
import sys
input = sys.stdin.readline

INF = 10**18

A, B, Q = map(int, input().split())
S = [-INF] + [int(input()) for _ in range(A)] + [INF]
T = [-INF] + [int(input()) for _ in range(B)] + [INF]

for _ in range(Q):
    x = int(input())
    si = bisect_left(S,x)
    ti = bisect_left(T,x)
    res = INF
    res = min(res, max(S[si] - x, T[ti] - x))
    res = min(res, max(x - S[si - 1], x - T[ti - 1]))
    res = min(res, x + T[ti] - 2 * S[si - 1])
    res = min(res, -x + 2 * T[ti] - S[si - 1])
    res = min(res, x + S[si] - 2 * T[ti - 1])
    res = min(res, -x + 2 * S[si] - T[ti - 1])
    print(res)