n,m = map(int,input().split())
vve = [list(map(int,input().split())) for i in range(m)]
graph = [[] for i in range(n+1)]
for a,b,e in vve:
  graph[a].append((b,-e))
score = [10**15 for i in range(n+1)]
score[1] = 0
for j in range(n+1):
  flg = 0
  for i in range(m):
    v1,v2,e = vve[i]
    e = -e
    if score[v1] != 10**15 and score[v2] > score[v1]+e:
      score[v2] = score[v1]+e
      flg = 1
      if j == n-1:
        p = -score[n]
      if j == n:
        q = -score[n]
  if flg == 0:
    break
if flg == 0:
  print(-score[n])
else:
  if p == q:
    print(p)
  else:
    print("inf")