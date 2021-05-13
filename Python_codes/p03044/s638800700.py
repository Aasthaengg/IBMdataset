n=int(input())
e=[[] for _ in range(n)]
for _ in range(n-1):
    xi,yi,wi=map(int, input().split())
    xi-=1;yi-=1
    e[yi].append((xi,wi))
    e[xi].append((yi,wi))

c=[0]*n
used=[0]*n

from collections import deque

q=deque()
q.append(0)
while q:
    u=q.popleft()
    for v,w in e[u]:
        if not used[v]:
            c[v]=(c[u]+w)%2
            used[v]=1
            q.append(v)
for i in c:
    print(i)