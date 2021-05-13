X,K,D = map(int, input().split())
X=abs(X)
if X>=K*D:
  print(X-K*D)
else:
  y=X//D
  z=K-y
  j=y*D
  if z%2==0:
    print(X-j)
  else:
    print(abs(X-j-D))
