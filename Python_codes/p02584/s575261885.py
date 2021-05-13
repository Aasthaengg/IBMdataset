x,k,d= map(int,input().split())
x=abs(x)
if x>d*k:
  print(x-d*k)
else:
  m=x//d
  k=(k-m)%2
  print(abs((x%d)-k*d))