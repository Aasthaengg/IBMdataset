#幅優先探索(BFS)
import sys
input = sys.stdin.readline

n,x,y = [int(x) for x in input().split()] # nは頂点の数、mは辺の数
g = [[] for _ in range(n)] # 隣接リスト

for i in range(n-1):
    a,b = i,i+1
    g[a].append(b)
    g[b].append(a)
g[x-1].append(y-1)
g[y-1].append(x-1)

from collections import deque

def bfs(u):
    queue = deque([u])
    d = [None] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d

# 0からの各頂点の距離
di = [0]*n
for i in range(n):
    l = bfs(i)
    for j in l:
        if j == 0:
            continue
        di[j-1] += 1
di = di[:-1]
for k in di:
    print(k//2)
