m, n = map(str, input().split())
if m*int(n)<=n*int(m):
  print(m*int(n))
else:
  print(n*int(m))