import sys
input=sys.stdin.readline

n,m = map(int, input().split())
link = [[] for _ in range(n)]
for i in range(m):
    tmp = list(map(int,input().split()))
    link[tmp[0]-1].append([tmp[1]-1,tmp[2]])
    link[tmp[1]-1].append([tmp[0]-1,-tmp[2]])
from collections import deque
INF=10**10
dist=[INF]*n
for i in range(n):
    if dist[i]!=INF:
        continue
    dist[i]=0
    Q = deque()
    Q.append([i,0])
    while Q:
        now,cnt = Q.popleft()
        for nxt,nxt_dist in link[now]:
            if dist[nxt] == INF:
                dist[nxt] = cnt+nxt_dist
                Q.append([nxt,cnt+nxt_dist])
            elif dist[nxt] != cnt+nxt_dist:
                    print("No")
                    exit()

print("Yes")