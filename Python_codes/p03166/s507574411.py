import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())
G = [[] for i in range(N)]
indegree = [0 for i in range(N)]

for i in range(M):
  x,y = map(int,readline().split())
  G[x - 1].append(y - 1)
  indegree[y - 1] += 1
  
stack = []
for i in range(len(indegree)):
  if indegree[i] == 0:
    stack.append(i)
    
cnt = -1
while stack:
  cnt += 1
  newstack = []
  while stack:
    v = stack.pop()
    for child in G[v]:
      indegree[child] -= 1
      if indegree[child] == 0:
        newstack.append(child)
  stack = newstack

print(cnt)