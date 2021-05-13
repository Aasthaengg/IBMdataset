import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    edge[v - 1].append([w, u - 1])
    edge[u - 1].append([w, v - 1])

# O(ElogV)
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

d = dijkstra(0)
ans = [0]*n

for i in range(n):
    if d[i] % 2 == 1:
        ans[i] = 1

for i in ans:
    print(i)