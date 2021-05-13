from collections import deque

N, M, R = map(int, input().split())
Rs = set(map(int, input().split()))

mp = [[float('inf')]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
  mp[i][i] = 0

for _ in range(M):
  a,b,c = map(int, input().split())
  mp[a][b] = c
  mp[b][a] = c
  
for k in range(1,N+1):
  for i in range(1,N+1):
    for j in range(1,N+1):
      mp[i][j] = min(mp[i][j], mp[i][k]+mp[k][j])

rlt = float('inf')
h = deque([])
for r in Rs:
  h.append([r])
  
while h:
  t = h.pop()
  if len(t) == R:
    tmp = 0
    for i in range(R-1):
      tmp += mp[t[i]][t[i+1]]
    rlt = min(rlt, tmp)
  else:
    for r in Rs:
      if r not in t:
        u = t + [r]
        h.append(u)

print(rlt)