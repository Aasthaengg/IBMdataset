import math

a,p=(map(int,input().split()))
if a>0:
  p=int(a*3+p)
elif a==0:
  pass
if p%2==1:
  print(math.floor(p/2))
else:
  print(int(p/2))