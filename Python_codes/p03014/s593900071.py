h,w = map(int, input().split())
g = []
for _ in range(h):
  g.append(input())
l = [[0 for i in range(w)] for j in range(h)]
r = [[0 for i in range(w)] for j in range(h)]
d = [[0 for i in range(w)] for j in range(h)]
u = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
  for j in range(w):
    if g[i][j] == '#':
      l[i][j] = 0
      u[i][j] = 0
    else:
      if j == 0:
        l[i][j] = 1
      else:
        l[i][j] = l[i][j-1]+1
      if i == 0:
        u[i][j] = 1
      else:
        u[i][j] = u[i-1][j]+1
for i in reversed(range(h)):
  for j in reversed(range(w)):
    if g[i][j] == '#':
      r[i][j] = 0
      d[i][j] = 0
    else:
      if j == w-1:
        r[i][j] = 1
      else:
        r[i][j] = r[i][j+1]+1
      if i == h-1:
        d[i][j] = 1
      else:
        d[i][j] = d[i+1][j]+1
ans = 0
for i in range(h):
  for j in range(w):
    ans = max(l[i][j]+r[i][j]+u[i][j]+d[i][j]-3,ans)
print(ans)