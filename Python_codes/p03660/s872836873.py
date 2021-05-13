import queue
n=int(input())
e=[[] for _ in range(n+1)]
for _ in range(n-1):
  a,b=map(int,input().split())
  e[a]+=[b]
  e[b]+=[a]
q=queue.Queue()
q.put(1)
vif=[-1]*n
vif[0]=0
while not q.empty():
  now=q.get()
  for to in e[now]:
    if vif[to-1]==-1:
      q.put(to)
      vif[to-1]=vif[now-1]+1
q.put(n)
vis=[-1]*(n+1)
vis[n-1]=0
while not q.empty():
  now=q.get()
  for to in e[now]:
    if vis[to-1]==-1:
      q.put(to)
      vis[to-1]=vis[now-1]+1
ans=0
for i in range(n):
  if vif[i]<=vis[i]:ans+=1
print(['Snuke','Fennec'][ans>n//2])