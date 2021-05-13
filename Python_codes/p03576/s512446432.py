import itertools

N, K = map(int, input().split())
X = []; Y = []
xy = []
for i in range(N):
  x, y= map(int, input().split())
  xy.append((x, y))
  X.append(x); Y.append(y)

ans = 10**20
x2 = list(itertools.combinations(X, 2))
y2 = list(itertools.combinations(Y, 2))

for xi, xj in x2:
  if xj < xi:
    xi, xj = xj, xi
  for yi, yj in y2:
    if yj < yi:
      yi, yj = yj, yi
    n = 0
    for x, y in xy:
      if xi<=x<=xj and yi<=y<=yj:
        n += 1
    if n >= K:
      ans = min(ans, (xj-xi)*(yj-yi))

print(ans)