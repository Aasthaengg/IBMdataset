from bisect import bisect_left
import sys
input = sys.stdin.readline

a, b, q = map(int, input().split())
INF = 10**12
s = [-INF] + [int(input()) for i in range(a)] + [INF]
t = [-INF] + [int(input()) for i in range(b)] + [INF]


for _ in range(q):
    x = int(input())
    k = bisect_left(s, x)
    l = bisect_left(t, x)
    sm = x - s[k - 1]
    sM = s[k] - x
    tm = x - t[l - 1]
    tM = t[l] - x
    ans = min(2 * sm + tM, 2 * sM + tm, 2 * tm + sM, 2 * tM + sm, max(sm, tm), max(sM, tM))
    print(ans)
