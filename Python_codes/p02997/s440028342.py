n, k = map(int, input().split())

if k <= (n - 1) * (n - 2) // 2:
    g = [[0] * (n + 1) for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            g[u][v] = 1

    cnt = n - 1
    for u in range(2, n + 1):
        for v in range(u + 1, n + 1):
            if k:
                g[u][v] = 0
                k -= 1
            cnt += g[u][v]

    print(cnt)
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if g[u][v]:
                print(u, v)

else:
    print(-1)
