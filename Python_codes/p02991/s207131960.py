from collections import deque

n,m=list(map(int,input().split()))
g=[[] for _ in range(10*(n+1)+3)]


for _ in range(m):
    u,v=list(map(int,input().split()))
    g[10*u].append(10*v+1)
    g[10*u+1].append(10*v+2)
    g[10*u+2].append(10*v)

s,t=list(map(int,input().split()))
inf=10**10
q=deque([10*s])
d=[inf]*(10*(n+1)+3)
d[10*s]=0

while len(q)>0:
    u=deque.pop(q)
    res=u%10
    for i in range(3):
        nres=(res+i)%3
        for v in g[u]:
            if d[v]<inf:
                continue
            d[v]=min(d[v],d[u]+1)
            deque.appendleft(q,v)

if d[10*t]==inf:
    print(-1)
else:
    print(d[10*t]//3)