X = int(input())

N, r = divmod(X, 100)

if r <= 5*N:
  print(1)
else:
  print(0)