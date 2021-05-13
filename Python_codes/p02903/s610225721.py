H,W,l1,l2=list(map(int,input().split()))
import numpy as np
l=np.zeros((H,W))
if l2>0:
   l[0:l2,l1:]=1
if l1>0:
   l[l2:,0:l1]=1
for i in l:
   print(*list(map(int,i)),sep="")