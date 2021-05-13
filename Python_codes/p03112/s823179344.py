from bisect import bisect_left

INF = 10 ** 11

a, b, q = map(int, input().split())
s = [-INF] + [int(input()) for _ in range(a)] + [INF]
t = [-INF] + [int(input()) for _ in range(b)] + [INF]
x = [int(input()) for _ in range(q)]

for e in x:
    si = bisect_left(s, e)
    ti = bisect_left(t, e)

    ans = INF
    for ss in [s[si-1], s[si]]:
        for tt in [t[ti-1], t[ti]]:
            d1 = abs(e - ss) + abs(ss - tt)
            d2 = abs(e - tt) + abs(tt - ss)
            ans = min(ans, d1, d2)

    print(ans)
