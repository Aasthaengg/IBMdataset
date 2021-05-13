n, k = map(int, input().split())
c = (n//k)**3
if k%2:
  print(c)
else:
  m = ((n-k//2)//k) + 1
  c += m**3
  print(c)