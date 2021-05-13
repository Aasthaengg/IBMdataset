import math
def C(n,r):
  if n<0 or r<0 or n-r<0:
    return 0
  else:
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
 
n,k=map(int,input().split())
for i in range(1,k+1):
  print(C(n-k+1,i)*C(k-1,i-1)%(10**9+7))