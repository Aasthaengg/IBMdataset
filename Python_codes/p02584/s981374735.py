X,K,D = map(int,input().split())
X = abs(X)
if K*D>X:
  r = X%D
  K -= (X-r)/D
  if K%2 == 0:
    print(r)
  else:
    print(abs(r-D))
else:
  print(X-(K*D))