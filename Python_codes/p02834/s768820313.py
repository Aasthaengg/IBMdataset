from collections import deque
N,u,v = map(int,input().split())
G = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
distT = [0 for _ in range(N+1)]
heap = deque([(u,0)])
distT[u] = 0
hist = [0 for _ in range(N+1)]
hist[u] = 1
while heap:
    x,d = heap.popleft()
    for y in G[x]:
        if hist[y]==0:
            distT[y] = d+1
            heap.append((y,d+1))
            hist[y]=1
heap = deque([(v,0)])
distA = [0 for _ in range(N+1)]
heap = deque([(v,0)])
distA[v] = 0
hist = [0 for _ in range(N+1)]
hist[v] = 1
while heap:
    x,d = heap.popleft()
    for y in G[x]:
        if hist[y]==0:
            distA[y]=d+1
            heap.append((y,d+1))
            hist[y] = 1
cmax = 0
for i in range(1,N+1):
    if distT[i]<=distA[i] and distA[i]>cmax:
        cmax = distA[i]
print(cmax-1)