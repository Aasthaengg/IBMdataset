import heapq
INFTY = 10**6
N,M = map(int,input().split())
G = {}
for _ in range(M):
    a,b,c = map(int,input().split())
    if a not in G:
        G[a] = []
    G[a].append((b,c))
    if b not in G:
        G[b] = []
    G[b].append((a,c))
F = {}
for s in range(1,N+1):
    F[s] = {}
    d = [INFTY for _ in range(N+1)]
    d[s] = 0
    hist = [0 for _ in range(N+1)]
    heap = [(0,s)]
    while heap:
        cur = heapq.heappop(heap)
        hist[cur[1]] = 1
        for x in G[cur[1]]:
            if hist[x[0]]==0:
                if d[x[0]]>cur[0]+x[1]:
                    d[x[0]] = cur[0]+x[1]
                    F[s][x[0]] = cur[1]
                    heapq.heappush(heap,(d[x[0]],x[0]))
E = []
for s in range(1,N+1):
    for i in range(1,N+1):
        if i!=s:
            cur = i
            while cur!=s:
                j = F[s][cur]
                if (cur,j) in E or (j,cur) in E:
                    break
                else:
                    E.append((cur,j))
                cur = j
print(M-len(E))