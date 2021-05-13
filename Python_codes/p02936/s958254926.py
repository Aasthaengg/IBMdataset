n,q=map(int,input().split())
g=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b)
    g[b-1].append(a)
x=[0]*n
for i in range(q):
    p,X=map(int,input().split())
    x[p-1]+=X
from collections import deque
d=deque()
d.append(0)
y=[0]*n
while len(d)>=1:
    s=d.popleft()
    y[s]+=1
    for i in g[s]:
        if y[i-1]!=1:
            d.append(i-1)
            x[i-1]+=x[s]
print(*x)