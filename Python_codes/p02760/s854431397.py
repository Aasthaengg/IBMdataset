a=[list(map(int,input().split())) for _ in [0]*3]
n=int(input())
b=[int(input()) for _ in range(n)]

import numpy as np

for i in range(3):
  a[i]=[1 if x in b else 0 for x in a[i]]   

s_1=max(np.sum(a,axis=0))
s_2=max(np.sum(a,axis=1))
s_3=a[0][0]+a[1][1]+a[2][2]
s_4=a[0][2]+a[1][1]+a[2][0]

if max(s_1,s_2,s_3,s_4)==3:
  print("Yes")
else:
  print("No")