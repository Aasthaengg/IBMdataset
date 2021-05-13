from collections import deque
N = int(input())
E = {}
for i in range(N):
  E[i] = []
  
for i in range(N-1):
  a,b = list(map(int, input().split()))
  a,b = a-1, b-1
  E[a].append(b)
  E[b].append(a)

# DFS for tree

def dfs(startp, depth):
  visited = [False for i in range(N)]
  d = deque()
  d.append(startp)

  while len(d) > 0:
    p = d.pop()
    visited[p] = True
    for q in E[p]:
      if visited[q]:
        continue
      d.append(q)
      depth[q] = depth[p] + 1

distf = [0 for i in range(N)]
dists = [0 for i in range(N)]

dfs(0, distf)
dfs(N-1, dists)

#print(distf)
#print(dists)
cntf, cnts = 0,0
for i in range(N):
  if distf[i] <= dists[i]:
    cntf += 1
  else:
    cnts += 1
    
print("Fennec" if cntf > cnts else "Snuke")