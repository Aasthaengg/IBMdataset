H,W=list(map(int,input().split()))
inf=float("inf")
import numpy as np
mem=np.full((H,W),inf)
l=[list(input()) for i in range(H)]
for i in range(H):
   for j in range(W):
      if l[i][j]=="#":
         mem[i,j]=0
for i in range(W-1):
   mem[:,i+1]=np.minimum(mem[:,i]+1,mem[:,i+1])
for i in reversed(range(1,W)):
   mem[:,i-1]=np.minimum(mem[:,i-1],mem[:,i]+1)
for i in range(H-1):
   mem[i+1,:]=np.minimum(mem[i+1,:],mem[i,:]+1)
for i in reversed(range(1,H)):
   mem[i-1,:]=np.minimum(mem[i-1,:],mem[i,:]+1)
print(int(np.max(mem)))