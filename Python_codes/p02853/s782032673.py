X, Y = map(int, input().split())
if 1 <= X <= 3:
  x = 400000 - X*100000
else:
  x = 0
if 1 <= Y <= 3:
  y = 400000 - Y*100000
else:
  y = 0
if X == 1 and Y == 1:
  print(x + y + 400000)
else:
  print(x + y)