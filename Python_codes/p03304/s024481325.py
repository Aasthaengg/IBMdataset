n,m,d=map(int,input().split())
if d==0:
  t=1/n
  t*=(m-1)
  print(t)
else:
  t=((n-d)*2)/(n**2)
  t*=(m-1)
  print(t)
