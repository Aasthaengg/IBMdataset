def bfs(v):
  distance=[-1]*n
  distance[v]=0
  next=connection[v]
  next2=set()
  visited=[-1]*n
  visited[v]=1
  visitct=1
  ct=0
  while len(next)!=0 or visitct!=n:
    ct+=1
    for i in range(len(next)):
      distance[next[i]]=ct
      visited[next[i]]=1
      visitct+=1
      for j in range(len(connection[next[i]])):
        if visited[connection[next[i]][j]]==-1:
          next2.add(connection[next[i]][j])
    next=list(next2)
    next2=set()
  return distance

import sys
input = sys.stdin.readline
n=int(input())
l=[list(map(int,input().split())) for i in range(n-1)]
connection=[[] for i in range(n)]
for i in range(n-1):
  connection[l[i][0]-1].append(l[i][1]-1)
  connection[l[i][1]-1].append(l[i][0]-1)
 
f=bfs(0);s=bfs(n-1)
ctf=0;cts=0
for i in range(n):
  if f[i]<=s[i]:
    ctf+=1
  else:
    cts+=1
 
if ctf>cts:
  print('Fennec')
else:
  print('Snuke')