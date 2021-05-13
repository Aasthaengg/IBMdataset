a = list(map(int, input().split()))
if a[0] >= 13:
  print(a[1])
elif a[0] >= 6:
  print(int(a[1]/2))
else:
  print(0)