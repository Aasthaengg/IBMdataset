import math
N,M=map(int,input().split())
d=abs(N-M)
if d>1:
  print(0)
elif d==1:
  ans=math.factorial(N)*math.factorial(M)%(10**9+7)
  print(ans)
else:
  ans=math.factorial(N)*math.factorial(M)*2%(10**9+7)
  print(ans)