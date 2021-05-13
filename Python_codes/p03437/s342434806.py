X, Y = map(int, input().split())

if X == Y or X % Y == 0:
  print(-1)
else:
  start = X
  while start % Y == 0:
    start += X
  print(start)