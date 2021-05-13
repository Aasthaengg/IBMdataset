x, y = map(int, input().split())
if x == 3:
  x_cost = 100000
elif x == 2:
  x_cost = 200000
elif x == 1:
  x_cost = 300000
else:
  x_cost = 0

if y == 3:
  y_cost = 100000
elif y == 2:
  y_cost = 200000
elif y == 1:
  y_cost = 300000
else:
  y_cost = 0

print(x_cost + y_cost + 400000 if x_cost == y_cost == 300000 else x_cost + y_cost)