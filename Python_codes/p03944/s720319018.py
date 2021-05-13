w, h, n = map(int,input().split())

y_min = 0
y_max = h

x_min = 0
x_max = w

for i in range(n):
  x, y, a = map(int,input().split())

  if a == 1:
    x_min = max(x_min, x)

  if a == 2:
    x_max = min(x_max, x)

  if a == 3:
    y_min = max(y_min, y)

  if a == 4:
    y_max = min(y_max, y)

white = (y_max - y_min) * (x_max - x_min)
if (y_max - y_min)>=0 and (x_max - x_min)>=0:
  print(max(white, 0))
else:
  print(0)