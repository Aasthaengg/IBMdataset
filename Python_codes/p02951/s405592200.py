a = [int(s) for s in input().split()]
b = int(a[0] - a[1])
c = a[2] - b
if int(c) < 0:
  print("0")
else:
  print(c)