# ABC 168 D
from collections import deque

N,M=map(int,input().split())
G=[[] for _ in [0]*(N+1)]
for _ in [0]*M:
    a,b=map(int,input().split())
    G[a]+=[b]
    G[b]+=[a]

F=[-1]*(N+1)
q=deque()
q.append((1,1))
while q:
    room,par=q.popleft()
    if F[room]>0:
        continue
    F[room]=par
    for nroom in G[room]:
        q.append((nroom,room))
        
print('Yes')
print(*F[2:],sep='\n')