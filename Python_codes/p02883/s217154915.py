N,K=map(int, input().split())
A=list(map(int, input().split()))
F=list(map(int, input().split()))
A=sorted(A)
F=sorted(F)[::-1]
import numpy as np
a=np.array(A)
f=np.array(F)

low=-1
high=10**18

while high-low>1:
  d=(high+low)//2
  #0かa-d//fの大きい値を採用するnp.maximum　
  if np.maximum(0,a-d//f).sum()<=K:
    high=d
  else:
    low=d
print(high)