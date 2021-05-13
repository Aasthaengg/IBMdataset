h,w=map(int,input().split())
c=[list(map(int,input().split())) for _ in range(10)]
a=[list(map(int,input().split())) for _ in range(h)]
INF=10**18
for k in range(10):
  for i in range(10):
    if c[i][k] == INF:
      continue
    for j in range(10):
      if c[k][j] == INF:
        continue
      c[i][j] = min(c[i][j], c[i][k] + c[k][j])
ans=0
for i in a:
  for k in i:
    if k!=-1:
      ans+=c[k][1]
print(ans)