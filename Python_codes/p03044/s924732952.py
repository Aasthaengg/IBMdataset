import queue
n=int(input())
e=[[] for _ in range(n)]
INF=10**18
d=[INF]*n
for _ in range(n-1):
  v,u,w=map(int,input().split())
  e[v-1]+=[(u-1,w)]
  e[u-1]+=[(v-1,w)]
q=queue.Queue()
q.put(0)
d[0]=0
while not q.empty():
  now=q.get()
  for to,dis in e[now]:
    if d[to]==INF:
      d[to]=d[now]+dis
      q.put(to)
for i in d:
  print(i%2)