a = [int(i) for i in input().split()]
if (a[0] <= a[1]):
  print(str(a[0])*a[1])
elif (a[1] < a[0]):
  print(str(a[1])*a[0])
