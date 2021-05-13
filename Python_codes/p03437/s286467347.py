X, Y = map(int,input().split())
i = 1
while X < 1000000001:
  X *= i
  if(X%Y != 0):
    print(X)
    break
  i += 1
else:
  print(-1)