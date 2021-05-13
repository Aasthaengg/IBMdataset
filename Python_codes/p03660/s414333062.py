import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
from collections import deque
N=int(input())

graph=[[] for _ in range(N+1)]
for _ in range(N-1):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
#print(graph)

dist_f=[-1]*(N+1)
d=0
queue=[1]
while queue:  
  new_queue=set()
  for u in queue:
    dist_f[u]=d
    for v in graph[u]:
      if dist_f[v]==-1:
        new_queue.add(v)
        
  queue=list(new_queue)
  d+=1
#print(dist_f)

dist_s=[-1]*(N+1)
d=0
queue=[N]
while queue:  
  new_queue=set()
  for u in queue:
    dist_s[u]=d
    for v in graph[u]:
      if dist_s[v]==-1:
        new_queue.add(v)
        
  queue=list(new_queue)
  d+=1
#print(dist_s)

cnt_f,cnt_s=0,0
for i in range(1,N+1):
  if dist_f[i]<=dist_s[i]:
    cnt_f+=1
  else:
    cnt_s+=1

#print(cnt_f,cnt_s)
if cnt_f>cnt_s:
  print("Fennec")
else:
  print("Snuke")