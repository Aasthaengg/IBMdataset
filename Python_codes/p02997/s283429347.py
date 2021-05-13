n,k = map(int,input().split())
n -= 1
s = (n-1)*n//2
if k > s:
  print(-1)
else:    
  m = s-k+n
  print(m)
  for i in range(n):
    print(1,2+i)
    m -= 1
  if m > 0:
    for i in range(1,n):
      if m == 0:
          break
      for j in range(2,n-i+2):
        if m > 0:
          print(j,j+i)
          m -= 1