a = [int(s) for s in input().split()]
if a[0] > 12:
  print(a[1])
elif a[0] > 5:
  print(int(a[1] / 2))
else:
  print("0")