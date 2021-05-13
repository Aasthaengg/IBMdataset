import sys
input = sys.stdin.readline

import heapq
def dijkstra(s):
    # 始点sから各頂点への最短距離
    d = [float('inf')]*n
    d[s] = 0
    # 各頂点が訪問済みかどうか
    used = [False]*n
    used[s] = True
    # 仮の距離を記録するヒープ
    que = []
    for e in edge[s]:
        heapq.heappush(que, e)
    while que:
        minedge = heapq.heappop(que)
        if used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = True
        for e in edge[v]:
            if not used[e[1]]:
                heapq.heappush(que, [e[0] + d[v], e[1]])
    return d

################################
n = int(input()) #n:頂点数　w:辺の数
w = n - 1

edge = [[] for i in range(n)]
#edge[i] : iから出る道の[重み,行先]の配列
for i in range(w):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    z = 1
    edge[x].append([z,y])
    edge[y].append([z,x]) 

dis_from_f = dijkstra(0)
dis_from_s = dijkstra(n - 1)

cnt = 0
for i, j in zip(dis_from_f, dis_from_s):
    if i <= j:
        cnt += 1
if cnt > n - cnt:
    print("Fennec")
else:
    print("Snuke")