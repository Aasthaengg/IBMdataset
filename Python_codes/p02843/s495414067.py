X = int(input())
A = X // 100
B = X % 100
if B > 5*A:
  print(0)
else:
  print(1)