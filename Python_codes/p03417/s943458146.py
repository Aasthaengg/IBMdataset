n,m=map(int,input().split())

if n<m:
  n,m=m,n
if m==1:
  print(abs(n-2))
elif m==2:
  print(0)
else:
  print((m-2)*(n-2))
