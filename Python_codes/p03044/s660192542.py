import sys
sys.setrecursionlimit(10**9)
def dfs(parent,current,distance):
  global m
  m[current]=distance
  for child in graph[current]:
    if child[0]==parent:
      continue
    dfs(current,child[0],distance+child[1])
n=int(input())
graph=[]
for i in range(n+1):
  graph.append([])
m=[0]*(n+1)
for i in range(n-1):
  a,b,c=map(int,input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])
dfs(1,1,0)
for i in range(1,n+1):
  if m[i]%2==0:
    print(1)
  else:
    print(0)