import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

N, M, P = list(map(int, sys.stdin.readline().split()))
ABC = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

graph = [[] for _ in range(N)]
for a, b, c in ABC:
    graph[a - 1].append((b - 1, P - c))


def bellman_ford(graph, from_v, to_v):
    """
    到達できないなら INF、負閉路があったら -INF
    :param list of (list of (int, int)) graph: (to, cap) の隣接リスト
    :param int from_v:
    :param int to_v:
    :rtype: int
    """

    def reachable(graph, from_v):
        """
        graph 上で from_v から到達できるかどうかのリスト
        :param graph:
        :param from_v:
        """
        ret = [False] * len(graph)
        ret[from_v] = True
        stack = [from_v]
        while stack:
            v = stack.pop()
            for u, _ in graph[v]:
                if not ret[u]:
                    ret[u] = True
                    stack.append(u)
        return ret

    # from_v から到達でき、かつ to_v へ到達できる頂点のみ考える
    # これら以外には負閉路があっても関係ない
    vertices = []
    revs = [[] for _ in range(len(graph))]
    for v, ud in enumerate(graph):
        for u, d in ud:
            revs[u].append((v, d))
    for v, (r1, r2) in enumerate(zip(reachable(graph, from_v), reachable(revs, to_v))):
        if r1 & r2:
            vertices.append(v)

    dist = [float('inf')] * len(graph)
    dist[from_v] = 0
    updated = True
    for _ in range(len(graph) + 1):
        updated = False
        for v in vertices:
            for u, d in graph[v]:
                if dist[v] + d < dist[u]:
                    dist[u] = dist[v] + d
                    updated = True
        if not updated:
            break
    return -float('inf') if updated else dist[to_v]


ans = -bellman_ford(graph, 0, N - 1)
if ans == INF or ans == -INF:
    print(-1)
else:
    print(max(0, ans))
