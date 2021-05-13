import copy
h,w = map(int,input().split())
c = [list(map(int,input().split())) for i in range(10)]
G = [list(map(int,input().split())) for i in range(h)]
d = copy.deepcopy(c)

for k in range(10):
  for i in range(10):
    for j in range(10):
      d[i][j] = min(d[i][j],d[i][k]+d[k][j])

ans = 0
for i in range(h):
  for j in range(w):
    if G[i][j] != -1:
      ans += d[G[i][j]][1]
      
print(ans)