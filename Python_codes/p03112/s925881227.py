from bisect import bisect
import sys
input = sys.stdin.readline

A, B, Q = map(int, input().split())
INF = float('inf')
s = [-INF] + [int(input()) for _ in range(A)] + [INF]
t = [-INF] + [int(input()) for _ in range(B)] + [INF]
for _ in range(Q):
    x = int(input())
    i = bisect(s, x)
    j = bisect(t, x)
    ans = INF
    for a in [s[i-1], s[i]]:
        for b in [t[j-1], t[j]]:
            ans = min(ans, abs(a-x)+abs(b-a), abs(b-x)+abs(a-b))
    print(ans)
