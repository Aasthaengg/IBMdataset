from collections import deque

n,q=map(int,input().split())

g=[[] for i in range(n+1)]
for i in range(1,n):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
    

cnt=[0]*(n+1)
for i in range(q):
    p,x=map(int,input().split())
    cnt[p]+=x

q = deque([1])
visited=set()
while q:
    v = q.popleft()
    visited.add(v)
    for next_v in g[v]:
        if next_v not in visited:
            cnt[next_v]+=cnt[v]
            q.append(next_v)

print(*cnt[1:])
