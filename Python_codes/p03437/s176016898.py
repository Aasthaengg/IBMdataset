X,Y = map(int,input().split())
if  X == Y:
  print(-1)
  exit()
if X > Y and X % Y == 0:
  print(-1)
  exit()
for x in range(X,10**18+1,X):
  if x % Y != 0:
    print(x)
    exit()