import heapq
import sys
input = sys.stdin.readline

def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq) # リストを優先度付きキューに変換
    cost = [float('inf')] * n # 行ったことのないところはinf
    cost[s] = 0 # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]: # コストが現在のコストよりも高ければスルー
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost

n=10
H,W = map(int,input().split())
c = [list(map(int,input().split())) for _ in range(n)]
A = [list(map(int,input().split())) for _ in range(H)]

e = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        e[i].append((c[i][j], j))
        
mp = float('inf')
mplist = [mp]*n
for i in range(n):
    dist = dijkstra(i)
    mplist[i] = dist[1]

chgmp =0
for ih in range(H):
    for iw in range(W):
        if A[ih][iw]!=-1:
            chgmp += mplist[A[ih][iw]]
print(chgmp)
