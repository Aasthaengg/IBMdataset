import queue
n=int(input())
INF=10**18
e=[[] for _ in range(n+1)]
d=[INF]*(n+1)
for i in range(n-1):
  a,b,c=map(int,input().split())
  e[a].append((b,c))
  e[b].append((a,c))
q,k=map(int,input().split())
que=queue.Queue()
que.put(k)
d[k]=0
while not que.empty():
  x=que.get()
  for i,c in e[x]:
    if d[i]==INF:
      que.put(i)
      d[i]=d[x]+c
for _ in range(q):
  x,y=map(int,input().split())
  print(d[x]+d[y])