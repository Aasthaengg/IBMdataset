R,D,X = map(int,input().split())

for n in range(10):
  X = R*X-D
  print(X)