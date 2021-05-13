from collections import deque
n=int(input())
d=[-1]*(n+1)
d[1]=0
v=[[] for i in range(n+1)]
for i in range(n):
  a=list(map(int,input().split()))
  v[a[0]]=a[2:]
q=deque()
q.append(1)
while len(q)>0:
  curr=q.popleft()
  for i in v[curr]:
    if d[i]==-1:
      d[i]=d[curr]+1
      q.append(i)
for i in range(1,n+1):
  print(f'{i} {d[i]}')
