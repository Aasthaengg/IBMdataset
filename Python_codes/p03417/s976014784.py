n, m = map(int, input().split())

if n < m:
  n, m = m, n
if m == 1:
  if n == 1:
    print(1)
  else:
    print(n-2)
    
elif m == 2:
  print(0)
  
else:
  print(n*m-2*(n+m)+4)