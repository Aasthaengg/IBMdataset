n, k = map(int, input().split())

if k <= (n - 1) * (n - 2) // 2:
    g = [0] * (n * n)
    for i in range(n * n):
        u = i // n
        v = i % n
        if u < v:
            g[i] = 1

    i = 0
    for _ in range(k):
        while g[i] == 0 or i % n == n - 1:
            i += 1
        g[i] = 0

    cnt = sum(g)
    print(cnt)
    for i, e in enumerate(g):
        if e:
            u = i // n + 1
            v = i % n + 1
            print(u, v)

else:
    print(-1)
