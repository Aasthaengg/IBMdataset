r, D, X_1 = input().split()
r = int(r)
D = int(D)
x = int(X_1)
for i in range(10):
  x = r * x - D
  print(str(x))
