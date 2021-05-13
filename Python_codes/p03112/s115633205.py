from bisect import bisect_left
a, b, q = map(int, input().split())
inf = 10**18
shrine = [-inf] + [int(input()) for _ in range(a)] + [inf]
temple = [-inf] + [int(input()) for _ in range(b)] + [inf]

for _ in range(q):
    ans = inf
    x = int(input())
    index_s = bisect_left(shrine, x)
    index_t = bisect_left(temple, x)

    for s in [shrine[index_s-1], shrine[index_s]]:
        for t in [temple[index_t-1], temple[index_t]]:
            ans = min(
                ans,
                abs(x-s) + abs(s-t),
                abs(x-t) + abs(s-t)
            )

    print(ans)
