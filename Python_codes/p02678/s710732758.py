import queue
n,m=map(int,input().split())
e=[[] for _ in range(n+1)]
INF=10**18
d=[INF]*(n+1)
ans=[0]*(n+1)
for _ in range(m):
  a,b=map(int,input().split())
  e[a]+=[b]
  e[b]+=[a]
q=queue.Queue()
q.put(1)
d[1]=0
while not q.empty():
  now=q.get()
  for to in e[now]:
    if d[to]==INF:
      ans[to]=now
      d[to]=d[now]+1
      q.put(to)
print('Yes')
for i in ans[2:]:
  print(i)