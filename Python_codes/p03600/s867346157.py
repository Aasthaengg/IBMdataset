N = int(input())
dic = [0]*N
dist = [[float('inf')]*N for i in range(N)]
for i in range(N):
  dic[i] = [int(c) for c in input().split()]
  for j in range(N):
    dist[i][j] = dic[i][j]
ans = 0
log = []
for k in range(N):
  for i in range(N-1):
    for j in range(i+1,N):
      dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
for i in range(N-1):
  for j in range(i+1,N):
    if dist[i][j]<dic[i][j]:
      print(-1)
      import sys
      sys.exit()
    flag = False
    for k in range(N):
      if k==i or k==j:
        continue
      if dist[i][j] == dist[i][k]+dist[k][j]:
        flag = True
    if flag:
      continue
    ans += dic[i][j]
print(ans)
