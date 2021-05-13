from copy import deepcopy
from collections import deque
n, m = map(int, input().split())
G = [[] for _ in range(n)]
V = []
for i in range(m):
    a, b = list(map(lambda x: x-1, map(int, input().split())))
    G[a].append(b)
    G[b].append(a)
    V.append([a,b])

ans = 0
# 各辺について、除いた場合グラフが非連結になるか確かめる.
# 非連結ならば、適当な頂点から探索した時に到達できない頂点が存在する.
for i in range(m):
    _G = deepcopy(G)
    _G[V[i][0]].remove(V[i][1])
    _G[V[i][1]].remove(V[i][0])
    # BFS
    ## キューの初期化
    que = deque([0])
    ## 距離の初期化
    D = [-1]*n
    D[0] = 0
    ##キューが尽きるまで探索を行う
    while que:
        ### 現在地を取得.
        nw = que.popleft()
        ### 現在地から行けるところについて探索.
        for nx in _G[nw]:
            if D[nx]!=-1: continue
            D[nx] = D[nw]+1
            que.append(nx)
    if min(D) == -1:
        ans += 1
print(ans)