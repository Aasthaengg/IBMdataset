n,m=map(int,input().split())
a=n//2019
b=m//2019
if n*m%2019==0 or b-a>=1:
  print(0)
else:
  best=2018
  for c in range(n%2019,m%2019):
    for d in range(c+1,m%2019+1):
      if c*d%2019<best:
        best=c*d%2019
  print(best)