import sys
sys.setrecursionlimit(200000)


def input():
    return sys.stdin.readline()[:-1]


# Kから順に探索して、Kからの距離を求める
def dfs(v, parent=-1, distance=0):
    # Kから現在の位置までの距離を記録する
    sum_distance[v] = distance
    for i, j in tree[v]:
        if i == parent:
            continue
        dfs(i, v, distance+j)


N = int(input())

tree = [[] * N for i in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append([b, c])
    tree[b].append([a, c])

Q, K = map(int, input().split())

# 事前に各頂点から頂点Kまでの距離を求める
sum_distance = [0]*N
dfs(K-1)

# クエリを処理する。xからKまでとyからKまでの距離の合計を求める
for _ in range(Q):
    x, y = map(int, input().split())
    print(sum_distance[x-1]+sum_distance[y-1])
