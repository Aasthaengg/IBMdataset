import sys
input = sys.stdin.buffer.readline

n = int(input())
edge = [[] for _ in range(n)]
for i in range(n-1):
    a,b,c = map(int, input().split())
    a, b = a-1, b-1
    edge[a].append((c, b))
    edge[b].append((c, a))

q, k = map(int, input().split())
k -= 1

import heapq
INF = 10**18
def dijkstra_heap(s, edge, n):
    d = [INF] * n
    used = [True] * n #True: not used
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist,e)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,(e[0]+d[v],e[1]))
    return d

d = dijkstra_heap(k, edge, n)
for i in range(q):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    print(d[x]+d[y])
