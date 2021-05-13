X,N = map(int,input().split())
if  N == 0:
  print(X)
  exit()
array = sorted(list(map(int,input().split())))
if not X in array:
  print(X)
  exit()  
else:
  for i in range(1,200):
    X_plus = X + i
    X_pull = X - i
    if not X_pull in array:
      print(X_pull)
      exit()
    if not X_plus in array:
      print(X_plus)
      exit()