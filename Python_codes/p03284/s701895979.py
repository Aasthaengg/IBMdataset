n, k = map(int, input().split())
if n%k != 0:
  print((n//k)+1 - (n//k))
else:
  print(0)