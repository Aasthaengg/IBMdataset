from bisect import bisect_left

N, Q = map(int, input().split())
R = [tuple(map(int, input().split())) for i in range(N)]
R.sort(key=lambda r: r[2])
q = [int(input()) for _ in range(Q)]

ans = [-1] * Q
skip = [-1] * (Q + 1)

for s, t, x in R:
    l = bisect_left(q, s - x)
    r = bisect_left(q, t - x)
    while l < r:
        if skip[l] == -1:
            skip[l] = r
            ans[l] = x
            l += 1
        else:
            l = skip[l]
for i in range(Q):
    print(ans[i])