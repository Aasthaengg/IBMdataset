import math
n,m=map(int,input().split())
if abs(n-m)>=2:
  print(0)
elif abs(n-m)==1:
  print(math.factorial(n)*math.factorial(m)%(10**9+7))
else:
  print(math.factorial(n)*math.factorial(m)*2%(10**9+7))