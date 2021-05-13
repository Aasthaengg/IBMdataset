import sys
input = lambda: sys.stdin.readline().rstrip()
import bisect

A,B,Q = map(int, input().split())

INF = 10 ** 18

s = [-INF] + [int(input()) for _ in range(A)] + [INF]
t = [-INF] + [int(input()) for _ in range(B)] + [INF]

for i in range(Q):
    x = int(input())
    right_s = bisect.bisect_right(s, x)
    right_t = bisect.bisect_right(t, x)

    ans = INF
    
    for S in [s[right_s-1], s[right_s]]:
        for T in [t[right_t-1], t[right_t]]:
            ans = min(ans, abs(x-S) + abs(T-S), abs(x-T) + abs(S-T))

    print(ans)