def gcd(x, y):
  if y==0:return x
  else:return gcd(y,x%y)

X,Y=[int(i) for i in input().split()]
G=gcd(X,Y)
if G==Y:print(-1)
else :print(X)