import math
N,M=map(int,input().split())
X=math.factorial(N)%(10**9+7)
Y=math.factorial(M)%(10**9+7)
if abs(N-M)>=2:
  print(0)
elif N==M:
  print(X*Y*2%(10**9+7))
else:
  print(X*Y%(10**9+7))
