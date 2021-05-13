X, Y = list(map(int, input().split()))
if Y == 0:
  print(X)
else:
  P = list(map(int, input().split()))
  num = 0
  for i in range(Y + 1):
    num = X - i
    if num not in P:
      print(num)
      break
    num = X + i
    if num not in P:
      print(num)
      break
