N, M=map(int, input().split())
s=input()
t=input()
from math import gcd

g=gcd(N,M)

if g==1:
  ans=(N*M)//g
else:
  n=N//g
  m=M//g
  import numpy as np
  pn=np.arange(m, M, m)
  qm=np.arange(n, N, n)
  ans=(N*M)//g
  for i in range(len(pn)):
    if s[qm[i]]!=t[pn[i]]:
      ans=-1
      break
if s[0]!=t[0]:
  ans=-1
print(ans)
  
  
  
