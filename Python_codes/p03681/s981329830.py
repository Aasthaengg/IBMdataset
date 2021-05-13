import math
n, m = map(int, input().split())

if abs(n-m)>1:
  print(0)
elif n-m==1:
  print(int((math.factorial(n)*math.factorial(m))%(10**9+7)))
elif m-n==1:
  print(int((math.factorial(m)*math.factorial(n))%(10**9+7)))
elif n==m:
  print(int((math.factorial(n)*math.factorial(m)*2)%(10**9+7)))