n,m = map(int,input().split())
edge = []
for _ in range(m):
  a,b,c = map(int,input().split())
  edge.append((a,b,-c))
dis = [float("inf")]*(n+1)
dis[1] = 0
f = 0
for i in range(n):
  for a,b,c in edge:
    if dis[b] > dis[a] + c:
      dis[b] = dis[a] + c
      if i == n-1:
        f = 1
ans = dis[n]
if f:
  for _ in range(n):
    for a,b,c in edge:
      if dis[b] > dis[a] + c:
        dis[b] = dis[a] + c
        if b == n:
          print("inf")
          exit(0)
print(-ans)