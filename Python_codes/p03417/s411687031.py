n, m = map(int, input().split())
if m*n==1:
  print(1)
elif min(n,m)==1:
  print(n*m-2)
elif min(n,m)==2:
  print(0)
else:
  print((m-2)*(n-2))