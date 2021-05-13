import sys
readline = sys.stdin.readline

N = int(readline())
G = [[] for i in range(N)]

for i in range(N - 1):
  a,b = map(int,readline().split())
  G[a - 1].append(b - 1)
  G[b - 1].append(a - 1)
  
C = list(map(int,readline().split()))

def get_farest(x):
  dist = [-1] * N
  stack = [(x,-1,0)]
  while stack:
    v,parent,c = stack.pop()
    if dist[v] != -1:
      continue
    dist[v] = c
    for child in G[v]:
      if child == parent:
        continue
      stack.append([child, v, c + 1])
  maxv = -1
  maxi = -1
  for i in range(len(dist)):
    if dist[i] > maxv:
      maxv = dist[i]
      maxi = i
  return maxi

f = get_farest(0)
start = get_farest(f)

C = sorted(C, reverse = True)
from collections import deque
q = deque([])
q.append([start, -1])
ind = 0
ans = [None] * N
while q:
  v,parent = q.popleft()
  ans[v] = C[ind]
  ind += 1
  for child in G[v]:
    if child == parent:
      continue
    q.append([child, v])
  
print(sum(C[1:]))
print(*ans)