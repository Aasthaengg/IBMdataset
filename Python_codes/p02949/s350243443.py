# -*- coding: utf-8 -*-
import heapq
import sys
sys.setrecursionlimit(10**9)

# 全頂点からのゴールへの到達可能性を確認
# 頂点1からDFSしてNまできたら、それまでのパス全てについて到達可能に更新
# その後、到達可能な部分のみを新たな辺にして、ベルマンフォード
# 辺の重みは（C - P）
# 負閉路を検出したなら-1
# そうでなければNまでの距離


N, M , P = map(int,input().split())
ABC = [list(map(int,input().split())) for _ in range (M)]

Edge = [[] for _ in range(N)]
for a,b,c in ABC:
    Edge[b-1].append(a-1)


reachable = [False]*N
reachable[N-1] = True

def dfs(v):
    for nv in Edge[v]:
        if reachable[nv]:
            continue
        else:
            reachable[nv] = True
            dfs(nv)
    return 

def BellmanFord(s, N, Edge):
    INF = 10**20
    dist = [INF] * N
    dist[s] = 0
    for i in range(N):
        isUpdated = False
        for t in range(N):
            if dist[t] == INF:
                continue
            for v,c in Edge[t]:
                if dist[t]+c < dist[v]:
                    dist[v] = dist[t]+c
                    isUpdated = True
        if not isUpdated:
            break
        elif i==N-1:
            return -1
    return dist

                
dfs(N-1)
newEdge = [[] for _ in range(N)]
for a,b,c in ABC:
    if reachable[a-1]:
        newEdge[a-1].append([b-1, P-c])

dist = BellmanFord(0, N, newEdge)
if dist==-1:
    print(-1)
else:
    print(max(0, -dist[N-1]))




