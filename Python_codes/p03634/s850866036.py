from collections import deque

n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    edge[a-1].append((b-1,c))
    edge[b-1].append((a-1,c))

q,k = map(int,input().split())

dist = [float('inf')] * n
visited = [0] * n

dist[k-1] = 0
visited[k-1] = 1
vq = deque([k-1])

while vq:
    
    vs = vq.popleft()
    
    for ve,vc in edge[vs]:
        if visited[ve] == 1: continue
        
        dist[ve] = dist[vs] + vc
        visited[ve] = 1
        vq.append(ve)


for _ in range(q):
    x,y = map(int,input().split())
    print(dist[x-1] + dist[y-1])