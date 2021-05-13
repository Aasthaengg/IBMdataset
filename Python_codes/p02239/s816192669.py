from collections import deque

N = int(input())

edge = [[] for _ in range(N)]
for _ in range(N):
    t = list(map(int,input().split()))
    if t[1] != 0:
        edge[t[0]-1] = list(map(lambda x:int(x)-1, t[2:]))

dist = [-1]*N
dist[0] = 0
        
q = deque([0])
while q:
    now = q.popleft()
    for nxt in edge[now]:
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + 1
            q.append(nxt)
        else:
            dist[nxt] = min(dist[nxt], dist[now] + 1)

for i,d in enumerate(dist):
    print(i+1, d)
