import itertools

n,k = map(int,input().split())
x = []
y = []
xy = []
for i in range(n):
  x0,y0 = map(int,input().split())
  x.append(x0)
  y.append(y0)
  xy.append((x0,y0))
x.sort()
y.sort()
xs = {}
ys = {}
for i in range(n):
  xs[x[i]] = i
  ys[y[i]] = i
m = [[0 for _ in range(n+1)] for _ in range(n+1)]
for x0,y0 in xy:
  m[ys[y0]+1][xs[x0]+1] += 1
for i in range(n):
  for j in range(n):
    m[i+1][j+1] += m[i][j+1]+m[i+1][j]-m[i][j]

ans = float('INF')
for x1,x2 in itertools.combinations(range(n),2):
  for y1,y2 in itertools.combinations(range(n),2):
    if k <= m[y2+1][x2+1]-m[y2+1][x1]-m[y1][x2+1]+m[y1][x1]:
      #print(x1,x2,y1,y2)
      ans = min((x[x2]-x[x1])*(y[y2]-y[y1]),ans)
print(ans)
#print(m)
