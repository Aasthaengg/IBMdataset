import sys
import heapq

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7
depth = [[] for _ in range(10 ** 5)]

def resolve():
    n = int(input())

    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        edge[a - 1].append([c, b - 1])
        edge[b - 1].append([c, a - 1])

    q, k = map(int, input().split())
    Query = [list(map(int, input().split())) for _ in range(q)]

    def dfs(v, p, d):
        depth[v] = d
        for c, u in edge[v]:
            if u == p:
                continue
            dfs(u, v, d + c)

    # 各頂点からkまでの最短距離を計算
    dfs(k - 1, -1, 0)

    # xからk,kからyの最短距離を足す
    for x, y in Query:
        res = depth[x - 1] + depth[y - 1]
        print(res)


if __name__ == '__main__':
    resolve()
