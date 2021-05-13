X, Y = map(int, input().split())
if X%Y == 0:
  print(-1)
  exit()
r = X*(Y-1)
print(r)
