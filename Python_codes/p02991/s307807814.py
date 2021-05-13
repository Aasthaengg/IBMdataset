N,M=map(int,input().split())
edge=[list(map(int,input().split())) for i in range(M)]
inf=10**20
c=[[] for i in range(N*3+1)]
for i,j in edge:
    c[i].append(N+j)
    c[N+i].append(N+N+j)
    c[N+N+i].append(j)
S,T=map(int, input().split())
from collections import deque
d=[inf]*(N*3+1)
d[S]=0
q=deque([S])
x=1
while q:
    q2=deque()
    for i in q:
        for j in c[i]:
            if d[j]>x:
                d[j]=x
                q2.append(j)
    q=q2
    x+=1
print(d[T]//3 if d[T]<inf else -1)
