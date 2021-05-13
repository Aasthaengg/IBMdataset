a = [int(input()) for i in range(4)]
if a[0] <= a[1]:
  print(a[0] * a[2])
else:
  print(a[1] * a[2] + (a[0] - a[1]) * a[3])