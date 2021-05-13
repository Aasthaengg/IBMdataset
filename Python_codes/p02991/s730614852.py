from collections import*
n,m=map(int,input().split())
e=[[]for _ in range(3*(n+1))]
d=[-3]*(3*(n+1))
for _ in range(m):
  a,b=map(int,input().split())
  e[a]+=[b+n]
  e[a+n]+=[b+2*n]
  e[a+2*n]+=[b]
s,t=map(int,input().split())
q=deque([s])
d[s]=0
while q:
  now=q.popleft()
  for to in e[now]:
    if d[to]!=-3:continue
    d[to]=d[now]+1
    q.append(to)
print(d[t]//3)