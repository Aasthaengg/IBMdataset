N,M,X,Y = map(int,input().split())
x = max(X,max(map(int,input().split())))
y = min(Y,min(map(int,input().split())))

if x<y:
  print("No War")
else:
  print("War")