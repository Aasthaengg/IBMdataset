r,D,x0=map(int,input().split())
X=[x0]
for _ in range(10):
  X.append(0)
for i in range(10):
  X[i+1]=r*X[i]-D
for i in range(1,11):
  print(X[i])