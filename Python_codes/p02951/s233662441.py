a = list(map(int, input().split()))
A = a[2]-(a[0]-a[1])
if A < 0:
  print(0)
else:
  print(A)