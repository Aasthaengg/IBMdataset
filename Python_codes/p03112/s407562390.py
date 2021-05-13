import sys
input = lambda: sys.stdin.readline().rstrip()
import bisect


A, B, Q = map(int, input().split())

INF = float("inf")

s = [-INF] + [int(input()) for _ in range(A)] + [INF]
t = [-INF] + [int(input()) for _ in range(B)] + [INF]

for i in range(Q):
    ans = INF
    x = int(input())
    s_right = bisect.bisect_right(s, x)
    t_right = bisect.bisect_right(t, x)

    s_left = s_right - 1
    t_left = t_right - 1

    for S in (s[s_left], s[s_right]):
        for T in (t[t_left], t[t_right]):
            ans = min(ans, abs(x-S) + abs(T-S), abs(x-T) + abs(S-T))

    print(ans)