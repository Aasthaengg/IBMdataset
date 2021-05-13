a = list(map(int,input().split()))
b = abs(a[0]-a[1])
c = abs(a[0]-a[2])

if b <= c:
  print("A")
else:
  print("B")