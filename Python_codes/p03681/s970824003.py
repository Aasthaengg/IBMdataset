from math import factorial
n,m=map(int,input().split())
p=10**9+7
if abs(n-m)>1:
  print(0)
else:
  if n==m:
    print((factorial(n)**2*2)%p)
  else:
    print((factorial(min(n,m))**2*max(n,m))%p)