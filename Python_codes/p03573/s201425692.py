a = list(map(int,input().split()))

if a.count(a[0]) == 1:
  print(a[0])
elif a.count(a[1]) == 1:
  print(a[1])
else:
  print(a[2])