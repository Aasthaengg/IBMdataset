# ABC138 D 
import sys
sys.setrecursionlimit(3*10**5)

res=0
INF=10**9
from collections import deque

f=lambda:map(int,input().split())
N,Q=f()
G=[[] for _ in [0]*(N+1)]
for i in range(N-1):
    a,b=f()
    G[a].append(b)
    G[b].append(a)

def bfs(a):
    q=deque()
    q.append(a)
    d=[INF]*(N+1)
    d[a]=0
    res=0
    while q:
        r=q.popleft()
        for nr in G[r]:
            if d[nr]==INF:
                q.append(nr)
                d[nr]=d[r]+1
                res+=1
    return d

d=bfs(1)

late=[0]*(N+1)
for _ in [0]*Q:
    p,x=f()
    late[p]+=x
    


S=[0]*(N+1)
q=deque()
q.append((1,0))
while q:
    node,par=q.popleft()
    S[node]+=late[node]
    for p in G[node]:
        if p==par:
            continue
        late[p]+=late[node]
        q.append((p,node))
        
print(*S[1:],sep='\n')