import bisect

A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
for _ in range(Q):
    x = int(input())
    sr = min(bisect.bisect_left(S, x), A - 1)
    sl = max(sr - 1, 0)
    tr = min(bisect.bisect_left(T, x), B - 1)
    tl = max(tr - 1, 0)
    print(min(abs(x - S[sl]) + abs(S[sl] - T[tl]),
              abs(x - S[sl]) + abs(S[sl] - T[tr]),
              abs(x - S[sr]) + abs(S[sr] - T[tl]),
              abs(x - S[sr]) + abs(S[sr] - T[tr]),
              abs(x - T[tl]) + abs(T[tl] - S[sl]),
              abs(x - T[tl]) + abs(T[tl] - S[sr]),
              abs(x - T[tr]) + abs(T[tr] - S[sl]),
              abs(x - T[tr]) + abs(T[tr] - S[sr])))
