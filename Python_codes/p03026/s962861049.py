from collections import Counter
from collections import deque
n = int(input())

counter = [0]*n
G = [[] for _ in range(n)]
for i in range(n-1):
  a,b = map(int,input().split())  
  G[a-1].append(b-1)
  G[b-1].append(a-1)
  counter[a-1] += 1
  counter[b-1] += 1
  
C = sorted(list(map(int,input().split())))[::-1]


root = 0
v = 0
for i in range(n):
  if v > counter[i]:
    root = i
    v = counter[i]


def bfs(s):
  que = deque()
  que.append(s)
  nodes = [-1]*n
  k = 0
  ans = 0
  while len(que)>0:    
    q = que.pop()    
    nodes[q] = C[k]    
    k += 1
    
    for v in G[q]:
      if nodes[v]<0:
        que.append(v)
  
  print(sum(C[1:]))
  print(*nodes)                

bfs(root)
