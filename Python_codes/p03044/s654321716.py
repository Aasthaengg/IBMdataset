def d_even_relation_dfs():
    import sys
    sys.setrecursionlimit(10**6)
    N = int(input())
    Edges = [[int(i) for i in input().split()] for j in range(N - 1)]

    graph = [[] for _ in range(N)]
    for u, v, w in Edges:  # 頂点は 0-indexed とする
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))

    def distance_from_root(parent, current, distance, ret=None):
        """根 (頂点 0) から各頂点への距離"""
        if ret is None:
            ret = [0] * N

        ret[current] = distance
        for next_vertex, dist in graph[current]:
            if next_vertex != parent:
                distance_from_root(current, next_vertex, distance + dist, ret)
        return ret
    ans = (0 if d % 2 else 1 for d in distance_from_root(-1, 0, 0))  # 根の親は -1 番
    return ' '.join(map(str, ans))

print(d_even_relation_dfs())