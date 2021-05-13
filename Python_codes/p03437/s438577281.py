X , Y = map(int, input().split())

if X%Y == 0:
  print(-1)
else:
  i = 2
  while True:
    if X*i > 10**18:
      print(-1)
      break
    if X*i%Y != 0:
      print(X*i)
      break
    i += 1