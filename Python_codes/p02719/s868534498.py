n,k = map(int, input().split())
mi = n%k
if mi > abs(mi-k):
  print(abs(mi-k))
else:
  print(mi)