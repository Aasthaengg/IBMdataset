X,Y=map(int,input().split())

if X%Y==0:
  print(-1)
else:
  if Y==2:
    print(X*3)
  else:
    print(X*(Y-1))