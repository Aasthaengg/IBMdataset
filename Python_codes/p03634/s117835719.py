def main():
    from collections import defaultdict
    import sys
    sys.setrecursionlimit(1000000)
    n, *rem = map(int, open(0).read().split())
    t = 3 * (n - 1)
    abc = rem[:t]
    q, k = rem[t], rem[t + 1]
    xy = rem[t + 2:]

    m = [[] for _ in range(n + 1)]
    dist = defaultdict(dict)
    for a, b, c in zip(*[iter(abc)] * 3):
        m[a].append(b)
        m[b].append(a)

        dist[a].update({b: c})
        dist[b].update({a: c})

    vis = [False] * (n + 1)
    cost = [0] * (n + 1)
    vis[k] = True

    def dfs(frm, to):
        if vis[to]:
            return
        vis[to] = True
        cost[to] = cost[frm] + dist[frm][to]
        frm = to
        for to in m[frm]:
            dfs(frm, to)

    frm = k
    for to in m[frm]:
        dfs(frm, to)

    tmp = []
    for x, y in zip(*[iter(xy)] * 2):
        tmp.append(cost[x] + cost[y])

    ans = "\n".join(map(str, tmp))
    print(ans)


if __name__ == '__main__':
    main()
