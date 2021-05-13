n,m = map(int,input().split())
if n==1 or m==1:
  print(max(max(m,n)-2,1))
else:
  n = n-2
  m = m-2
  print(n*m)