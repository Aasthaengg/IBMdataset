n,m,d=(int(x) for x in input().split())
if d==0:
  print((m-1)/n)
else:
  print(2*(n-d)/(n*n)*(m-1))
