#55 C - Cat Snuke and a Voyage
from collections import deque
N,M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

# BFS のためのデータ構造
dist = [-1]*N
que = deque([])

# 初期条件 (島 1 を初期ノードとする)
dist[0] = 0
que.append(0)

while (len(que) != 0):
    v = que.popleft()# キューから先頭頂点を取り出す
    for next_v in G[v]:
        if (dist[next_v] != -1):# next_v が探索済みならスルー
            continue
        #新たな頂点 next_v について情報を更新してキューに追加
        dist[next_v] = dist[v] + 1
        que.append(next_v)
        
if dist[N-1] == 2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')