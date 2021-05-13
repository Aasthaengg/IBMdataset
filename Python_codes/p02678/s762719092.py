import heapq
INFTY = 10**6
N,M = map(int,input().split())
G = {i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
dist = [INFTY for _ in range(N+1)]
hist = [0 for _ in range(N+1)]
heap = [(0,1)]
dist[1] = 0
hist[1] = 1
pre = {1:0}
while heap:
    d,x = heapq.heappop(heap)
    if d>dist[x]:continue
    for y in G[x]:
        if hist[y]==0:
            if dist[y]>d+1:
                dist[y] = d+1
                pre[y] = x
                heapq.heappush(heap,(d+1,y))
flag = 0
for i in range(1,N+1):
    if dist[i]>=INFTY:
        flag = 1
        break
if flag==1:
    print("No")
else:
    print("Yes")
    for i in range(2,N+1):
        print(pre[i])