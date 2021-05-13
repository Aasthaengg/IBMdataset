def main():
    import sys

    sys.setrecursionlimit(10 ** 7)

    input = sys.stdin.readline

    def dfs(v, d):
        for u in g[v]:
            if d[u] != init:
                continue
            d[u] = d[v] + 1
            dfs(u, d)

    n = int(input())

    g = tuple(set() for _ in range(n))
    for _ in range(n - 1):
        a, b = (int(x) - 1 for x in input().split())
        g[a].add(b)
        g[b].add(a)

    init = n

    dist_1 = [init] * n
    dist_1[0] = 0
    dfs(0, dist_1)

    dist_n = [init] * n
    dist_n[n - 1] = 0
    dfs(n - 1, dist_n)

    fennec = sum(dist_1[v] <= dist_n[v] for v in range(n))
    snuke = n - fennec

    if fennec > snuke:
        print('Fennec')
    else:
        print('Snuke')


if __name__ == '__main__':
    main()
