R,D,X = map(int,input().split())
a = X

for n in range(10):
  a = R*a-D
  print(a)