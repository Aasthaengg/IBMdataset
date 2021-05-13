x, y = map(int, input().split())

if x < y:
  print(x)
  exit()
  
if x % y != 0:
  print(x)
else:
  print(-1)