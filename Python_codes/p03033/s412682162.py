import sys
from bisect import bisect_left

input = sys.stdin.readline
n, q = map(int, input().split())
stx = [tuple(map(int, input().split())) for _ in range(n)]
d = [int(input()) for _ in range(q)]

stx.sort(key=lambda x: x[2])

ans = [-1] * q
jump = [-1] * q
for s, t, x in stx:
    d_start = bisect_left(d, s - x)
    d_stop = bisect_left(d, t - x, lo=d_start)
    while d_start < d_stop:
        if jump[d_start] == -1:
            ans[d_start] = x
            jump[d_start] = d_stop
            d_start += 1
        else:
            d_start = jump[d_start]

for an in ans:
    print(an)
