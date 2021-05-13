N, M=map(int, input().split())
if abs(N-M)>=2:
  print(0)
else:
  from math import factorial
  if abs(M-N)==1:
    r=0
  else:
    r=1
  ans=factorial(N)*factorial(M)*(2**r)
  ans=ans%(10**9+7)
  print(ans)