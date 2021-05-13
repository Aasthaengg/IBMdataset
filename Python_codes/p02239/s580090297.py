from collections import deque

n = int(input())
g = [list(map(int, input().split()))[2:] for _ in range(n)]
que = deque([0])
dist = [-1] * n
dist[0] = 0  # 初期条件
while que:  # queが空なるまで
    u = que.popleft()  # queの左から順に取り出す
    for v in g[u]:
        v -= 1  # 0-indexedに変更
        if dist[v] == -1:  # 未探索の時
            dist[v] = dist[u] + 1  # 最短距離を記録
            que.append(v)  # queに追加
for i in range(n):
    print(i + 1, dist[i])
