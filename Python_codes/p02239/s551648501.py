n = input()
  
d = [-1 for i in range(n)]
M = [[0 for i in range(n)] for j in range(n)]
color = [0 for i in range(n)]
  
def BFS(s):
  color[0] = 1
  q = []
  q.append(s)
  d[s] = 0
  while len(q) != 0:
    u = q[0]
    q.pop(0)
    for v in range(n):
      if M[u][v] == 1 and color[v] == 0:
        color[v] = 1
        d[v] = d[u] + 1
        q.append(v)
  color[u] = 2
  for i in range(n):
    print i+1, d[i]
  
for i in range(n):
  G = map(int, raw_input().split())
  for j in range(G[1]):
    M[G[0]-1][G[2+j]-1] = 1
  
BFS(0)