n, m = map(int, input().split())
a, b, c, d = [], [], [], []
for i in range(n) :
  ai, bi = map(int, input().split())
  a.append(ai), b.append(bi)
for i in range(m) :
  ci, di = map(int, input().split())
  c.append(ci), d.append(di)

for i in range(n) :
  cost, ans = 10**18, 0
  for j in range(m) :
    if cost > abs(a[i] - c[j]) + abs(b[i] - d[j]) :
      cost = abs(a[i] - c[j]) + abs(b[i] - d[j])
      ans = j+1
  print(ans)
