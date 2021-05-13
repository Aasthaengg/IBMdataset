n, m = map(int, input().split())
if n >= 2:
  if m >= 2:
    print((n-2) * (m-2)) 
  else:
    print((n-2) * m)
else:
  if m >= 2:
    print(n * (m-2)) 
  else:
    print(n * m) 