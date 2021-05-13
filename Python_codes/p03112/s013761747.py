from bisect import bisect_left, bisect_right
a, b, q = map(int, input().split())
inf = 10**18
shrine = [-inf] + [int(input()) for _ in range(a)] + [inf]
temple = [-inf] + [int(input()) for _ in range(b)] + [inf]

for _ in range(q):
    ans = inf
    x = int(input())
    index_s = bisect_left(shrine, x)
    index_t = bisect_right(temple, x)
    for i in range(index_s-1, index_s+1):
        s = shrine[i]
        i_t = index_t
        t0, t1 = temple[i_t-1], temple[i_t]
        ans = min(
            ans,
            abs(x - s) + abs(s - t0),
            abs(x - s) + abs(s - t1),
        )

    for i in range(index_t-1, index_t+1):
        t = temple[i]
        i_s = index_s
        s0 = shrine[i_s - 1]
        s1 = shrine[i_s]
        ans = min(
            ans,
            abs(x - t) + abs(t - s0),
            abs(x - t) + abs(t - s1),
        )

    print(ans)
