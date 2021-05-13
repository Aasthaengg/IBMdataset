import sys
input=sys.stdin.readline
N,M=map(int,input().split())

graph=[[] for _ in range(N+1)]
for i in range(M):
  u,v=map(int,input().split())
  graph[u].append(v)
  
S,T=map(int,input().split())

#print(graph)
visited=[]
for i in range(N+1):
  visited.append([False]*3)
  
queue=[S]
t=0
while queue:
  new_queue=set()
  for u in queue:
    if u==T and t%3==0:
      print(t//3)
      sys.exit(0)
    
    visited[u][t%3]=True
    for v in graph[u]:
      if not visited[v][(t+1)%3]:
        new_queue.add(v)
        
  queue=list(new_queue)
  t+=1
  
print(-1)