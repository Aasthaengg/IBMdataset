N, M, X, Y = list(map(lambda a: int(a), input().split(" ")))
x = list(map(lambda b: int(b), input().split(" ")))
y = list(map(lambda c: int(c), input().split(" ")))
x.append(X)
y.append(Y)
x.sort()
y.sort()
if x[-1] < y[0]:
  print("No War")
else:
  print("War")
