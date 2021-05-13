def p_f():
    from sys import stdin
    input = stdin.readline
    N, u, v = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(N - 1)]
    if u == v:
        print(0)
        exit()

    def BFS(K, edges, N):
        roots = [[] for i in range(N)]
        for a, b in edges:
            roots[a - 1] += [(b - 1, 1)]
            roots[b - 1] += [(a - 1, 1)]
        dist = [-1] * N
        stack = []
        stack.append(K)
        dist[K] = 0
        while stack:
            label = stack.pop(-1)
            for i, c in roots[label]:
                if dist[i] == -1:
                    dist[i] = dist[label] + c
                    stack += [i]
        return dist

    dist_v = BFS(v - 1, edges, N)
    dist_u = BFS(u - 1, edges, N)
    ans = 0
    for du, dv in zip(dist_u, dist_v):
        if du < dv and ans < dv - 1:
            ans = dv - 1
    print(ans)


if __name__ == '__main__':
    p_f()
