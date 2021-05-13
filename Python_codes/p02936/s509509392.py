n,q=map(int,input().split())
es=[[] for i in range(n)]
rank=[-1]*n
rank[0]=0
for i in range(n-1):
    a,b=map(int,input().split())
    es[a-1].append(b-1)
    es[b-1].append(a-1)

px=[0]*n
for i in range(q):
    p,x=map(int,input().split())
    px[p-1]+=x

score=[0]*n
score[0]=px[0]
from collections import deque
que=deque([0])
while que:
    s=que.popleft()
    for g in es[s]:
        if rank[g]==-1:
            rank[g]=rank[s]+1
            score[g]=score[s]+px[g]
            que.append(g)
print(*score)