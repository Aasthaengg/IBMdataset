import math
n,k=map(int,input().split())
a=list(map(int,input().split()))

x0, x1 = 0, 10**9
while x0 + 1  < x1:
  x = (x0+x1)//2
  suma=0
  for i in a:
    if i%x==0:
      suma+=(i//x)-1
    else:
      suma += (i//x)
    
  if suma > k:
    x0 = x
  else:
    x1 = x
print(x1)
