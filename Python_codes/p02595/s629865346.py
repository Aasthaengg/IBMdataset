n,d = [int(x) for x in input().split()]
x = []
y = []
for i in range(n):
  x1,y1 = [int(x) for x in input().split()]
  x.append(x1)
  y.append(y1)
c = 0
for i in range(n):
  s = x[i] ** 2 + y[i] ** 2
  if s <= d ** 2:
    c += 1
print(c)