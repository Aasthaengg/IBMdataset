a = [int(_) for _ in input().split()]
a.sort()
if a[0] == a[1]:
  print(a[2])
elif a[0] == a[2]:
  print(a[1])
else:
  print(a[0])