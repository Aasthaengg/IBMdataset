from collections import deque

# リストでグラフを表現する
n = int(input())
G = [input().split()[2:] for _ in range(n)]

# 頂点1から各頂点への距離を-1 (頂点1からたどり着けない)で初期化する
d = [-1] * n

que = deque()  # 訪問予定の頂点を格納する

# 初期状態をキューに入れる
que.append(0)
d[0] = 0

while que:
    p = que.popleft()  # FIFOでキューの要素を取り出し、その頂点を訪ねる。
    for v in G[p]:
        v = int(v) - 1
        if d[v] < 0:  # まだ訪れたことがない
            que.append(v)
            # 距離を記録する
            d[v] = d[p] + 1


for i in range(n):
    print(i+1, d[i])
