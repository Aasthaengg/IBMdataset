from collections import deque

N, Q = map(int, input().split())

# N個の頂点について、隣接要素を格納
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

# 各piにxiを追加しておく（子要素は見ない）
points = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    points[p - 1] += x

# 答え
result = [0] * N

# 訪れたら1, まだ訪れていなかったら0
visited = [0] * N
visited[0] = 1

# [ [頂点、累計ポイント], [頂点、累計ポイント], ...]
dq = deque([[0, points[0]]])

# 深さ優先探索(DFS)
while dq:
    node, count = dq.pop()
    result[node] = count
    # 今見ている頂点が持つ隣接要素について
    for ni in G[node]:
        # 未訪問の要素がある場合
        if visited[ni] != 1:
            visited[ni] = 1
            dq.append([ni, points[ni] + count])

print(*result)
