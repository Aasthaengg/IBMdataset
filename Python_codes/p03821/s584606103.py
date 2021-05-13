import numpy as np

N=int(input())
L=np.array([list(map(int,input().split())) for _ in range(N)])[::-1]
ans=0

for a,b in L:
  mod=(a+ans)%b
  if mod==0:
    continue
  else:
    ans+=b-mod
print(ans)