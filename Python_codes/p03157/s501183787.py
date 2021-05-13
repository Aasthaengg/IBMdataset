from collections import deque
H, W = map(int, input().split())
S = []
for i in range(H):
  S.append(list(input()))

V = {}
for i in range(H):
  for j in range(W):
    V[str(i) + "_" + str(j)] = []
    
for i in range(H):
  for j in range(W):
    
    for dy,dx in [(-1,0), (1,0), (0,-1), (0,1)]:
      y,x = i+dy, j+dx
      if y < 0 or H <= y or x < 0 or W <= x:
        continue
      if S[i][j] == S[y][x]:
        continue
      V[str(i) + "_" + str(j)].append([y,x])
      
ans = 0
visited = [[False for i in range(W)] for j in range(H)]
willsearch = [[False for i in range(W)] for j in range(H)]
Q = deque()
#print(V)
def dfs(y,x):
  wc, bc = 0, 0
  Q.append([y,x])
  while len(Q) > 0:
    b,a = Q.pop()
    #print("pop;", b, a, Q)
    visited[b][a] = True
    if S[b][a] == '.':
      wc += 1
    else:
      bc += 1
    for q,p in V[str(b) + "_" + str(a)]:
      #print("yeah:", q,p)
      if visited[q][p] or willsearch[q][p]:
        continue
      Q.append([q,p])
      willsearch[q][p] = True
    #print(b,a,"|",Q)
  #print(y,x,wc,bc)
  return wc*bc

for i in range(H):
  for j in range(W):
    ans += dfs(i,j)
    
print(ans)