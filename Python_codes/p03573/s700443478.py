X=list(map(int,input().split()))
Y=sorted(X)

if Y[0]==Y[1]:
  print(Y[2])
else:
  print(Y[0])