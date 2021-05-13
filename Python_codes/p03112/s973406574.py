from bisect import bisect_left
a, b, q = map(int, input().split())
s = []
for _ in range(a):
    s.append(int(input()))
t = []
for _ in range(b):
    t.append(int(input()))
INF = 10**12
for _ in range(q):
    x = int(input())
    s_l = t_l = -INF
    s_r = t_r = INF
    tmp = bisect_left(s, x)
    if tmp>0:
        s_l = s[tmp-1]
    if tmp<a:
        s_r = s[tmp]
    tmp = bisect_left(t, x)
    if tmp>0:
        t_l = t[tmp-1]
    if tmp<b:
        t_r = t[tmp]
    ans = min(
        x-min(s_l, t_l),
        max(s_r, t_r)-x,
        s_r-t_l+min(s_r-x, x-t_l),
        t_r-s_l+min(t_r-x, x-s_l)
    )
    print(ans)