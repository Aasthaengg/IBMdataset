# ABC133 E
from collections import deque
N,K=map(int,input().split())
p=10**9+7
G=[[] for _ in [0]*(N+1)]
for _ in [0]*(N-1):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)
    
D=[-1]*(N+1)
F=set()
color=[K]*(N+1)

res=1
D[1]=0
q=deque()
q.append(1)
while q:
    node=q.pop()
    if node in F:
        continue
    if D[node]>1:
        color[node]-=1
    if color[node]<=0:
        res*=0
    else:
        res=(res*color[node])%p
    F.add(node)
    i=1
    for next_node in G[node]:
        if D[next_node]>=0:
            continue
        D[next_node]=D[node]+1
        color[next_node]-=i
        i+=1
        q.append(next_node)
print(res%p)