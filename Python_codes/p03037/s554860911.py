n,m = map(int, input().split())
x = []
y = []
for _ in range(m):
  l,r = map(int, input().split())
  x.append(l)
  y.append(r)
x = max(x)
y = min(y)

if y-x >= 0: print(y-x+1)
else: print(0)