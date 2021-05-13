import math
import numpy as np

N,M=map(int,input().split())
gcd=math.gcd(N,M)
lcm=N*M//gcd

S=input()
T=input()
i=1

L=np.array([lcm*i for i in range(1,max(N,M)) if lcm*i<=N*M])
S_list=L//M
T_list=L//N

if S[0]!=T[0]:
  print(-1)
else:
  for i in range(len(S_list)-1):
    if S[S_list[i]]!=T[T_list[i]]:
      print(-1)
      break
  else:
    print(lcm)