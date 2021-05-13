from bisect import bisect_left

INF = 10 ** 11

a, b, q = map(int, input().split())
s = [-INF] + [int(input()) for _ in range(a)] + [INF]
t = [-INF] + [int(input()) for _ in range(b)] + [INF]
x = [int(input()) for _ in range(q)]

for e in x:
    si = bisect_left(s, e)
    ti = bisect_left(t, e)
    sl, sr = s[si-1], s[si]
    tl, tr = t[ti-1], t[ti]

    ans = INF
    ans = min(ans, e - min(sl, tl))
    ans = min(ans, max(sr, tr) - e)
    ans = min(ans, e - sl + tr - sl)
    ans = min(ans, e - tl + sr - tl)
    ans = min(ans, sr - e + sr - tl)
    ans = min(ans, tr - e + tr - sl)

    print(ans)
