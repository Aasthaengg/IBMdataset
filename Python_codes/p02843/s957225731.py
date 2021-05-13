X = int(input())
a = X // 100
r = X % 100
if r <= 5 * a:
  print("1")
else:
  print("0")