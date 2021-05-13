a = list(map(int, input().split()))
b= a[0] - a[1] * 2
if b <= 0:
  print(0)
else:
  print(b)