import heapq
INFTY = 10**6
N,M = map(int,input().split())
G = {i:[] for i in range(1,N+1)}
Arc = {}
for _ in range(M):
    a,b,c = map(int,input().split())
    G[a].append((b,c))
    G[b].append((a,c))
    Arc[(a,b)]=0
    Arc[(b,a)]=0
for s in range(1,N+1):
    dist = [INFTY for _ in range(N+1)]
    dist[s] = 0
    hist = [0 for _ in range(N+1)]
    heap = [(0,s)]
    pre = {}
    while heap:
        d,x = heapq.heappop(heap)
        if dist[x]<d:continue
        hist[x] = 1
        for y,e in G[x]:
            if hist[y]==0 and dist[y]>d+e:
                dist[y] = d+e
                pre[y] = x
                heapq.heappush(heap,(d+e,y))
    for j in pre:
        a = j
        while pre[a]!=s:
            b = pre[a]
            Arc[(a,b)] = 1
            Arc[(b,a)] = 1
            a = b
        Arc[(a,s)] = 1
        Arc[(s,a)] = 1
cnt = 0
for x in Arc:
    if Arc[x]==0:
        cnt += 1
print(cnt//2)