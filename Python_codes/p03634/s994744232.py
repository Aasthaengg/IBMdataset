n=int(input())
edges=[[] for i in range(n)]
for i in range(n-1):
    a,s,d=map(int,input().split())
    edges[a-1].append((s-1,d));edges[s-1].append((a-1,d))
q,k=map(int,input().split())
cost=[0]*n
from collections import deque
dq=deque([])
#pop/append/(append,pop)_left/in/len/count/[]/index/rotate()(右へnずらす)
for to,cos in edges[k-1]:
    dq.append((k-1,to))
    cost[to]=cos
while dq:
    par,now=dq.popleft()
    
    for to,c in edges[now]:
        if to!=par:
            cost[to]=cost[now]+c
            dq.append((now,to))

for i in range(q):
    x,y=map(int,input().split())
    print(cost[x-1]+cost[y-1])