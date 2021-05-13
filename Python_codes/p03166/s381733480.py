

INF = float('inf')


def tc():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        g[x].append(y)

    vis = [False] * (n + 1)
    done = [False] * (n + 1)

    stack = list(range(1, n + 1))
    topsort = []
    while stack:
        u = stack[-1]
        if done[u]:
            stack.pop()
            continue
        vis[u] = True

        leaf = True
        for v in g[u]:
            if not vis[v]:
                leaf = False
                stack.append(v)

        if leaf:
            topsort.append(u)
            done[u] = True
            stack.pop()  # if no vs, pop u

    # topsort.reverse() # topsort more useful backwards here
    dp = [0] * (n + 1)
    for u in topsort:
        if g[u]:
            dp[u] = max(dp[v] for v in g[u]) + 1

    print(max(dp))


tc()
