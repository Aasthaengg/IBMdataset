def Bellman_Ford(s, g, inf=1 << 60):
    # https://tjkendev.github.io/procon-library/python/graph/bellman-ford.html
    N = len(g)
    dist = [inf] * N
    dist[s] = 0
    for _ in range(N):
        not_updated = True
        for v in range(N):
            for u, c in g[v]:
                if (dist[v] == inf) or (dist[v] + c >= dist[u]): continue
                dist[u] = dist[v] + c
                not_updated = False

        if not_updated:
            return max(0, -dist[N - 1])

    # 負閉路が存在する
    for _ in range(N):
        not_updated = True
        for v in range(N):
            for u, c in g[v]:
                if (dist[v] == inf) or (dist[v] + c >= dist[u]): continue
                dist[u] = -inf
                not_updated = False
        if not_updated: break

    if dist[N - 1] == -inf:
        return -1
    else:
        return max(0, -dist[N - 1])


def main():
    import sys
    input = sys.stdin.readline

    N, M, P = map(int, input().split())

    g = tuple(set() for _ in range(N))
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        g[a].add((b, -(c - P)))  # to,coin(負辺)

    ret = Bellman_Ford(0, g)
    print(ret)


if __name__ == '__main__':
    main()
