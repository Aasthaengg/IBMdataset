from collections import deque
INFTY = 10**14+100
N = int(input())
T = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    a,b,c = map(int,input().split())
    T[a].append((b,c))
    T[b].append((a,c))
Q,K = map(int,input().split())
dist = [INFTY for _ in range(N+1)]
hist = [0 for _ in range(N+1)]
dist[K] = 0
hist[K] = 1
heap = deque([(K,0)])
while heap:
    x,d = heap.popleft()
    for y,d1 in T[x]:
        if hist[y]==0:
            heap.append((y,d+d1))
            dist[y] = d+d1
            hist[y]=1
for _ in range(Q):
    x,y = map(int,input().split())
    print(dist[x]+dist[y])