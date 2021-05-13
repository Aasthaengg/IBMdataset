a=[int(_) for _ in input().split()]
if a[0]%2==0 or a[1]%2==0 or a[2]%2==0:
  print(0)
else:
  a.sort()
  print(a[0]*a[1])
