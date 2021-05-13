def main():
    from collections import deque, defaultdict
    n, *uvw = map(int, open(0).read().split())
    l = defaultdict(dict)
    g = [[] for _ in range(n + 1)]

    for u, v, w in zip(uvw[::3], uvw[1::3], uvw[2::3]):
        g[u].append(v)
        g[v].append(u)
        l[u].update({v: w % 2})

    l[0].update({1: 0})

    vis = [False] * (n + 1)
    col = [0] * (n + 1)

    q = deque()
    q.append([0, 1, 0])

    while q:
        i, j, k = q.popleft()
        if vis[j]:
            continue
        vis[j] = True
        c = k if l[min(i, j)][max(i, j)] == 0 else 1 - k
        col[j] = c

        for x in g[j]:
            q.appendleft([j, x, c])

    print(*col[1:], sep='\n')


if __name__ == '__main__':
    main()
