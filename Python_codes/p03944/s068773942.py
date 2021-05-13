import numpy as np
W,H,N=map(int,input().split())

M = np.ones(W*H).reshape(H,W)

for i in range(N):
  x,y,a =map(int,input().split())
  if a==1:
    M[:,:x]=0
  if a==2:
    M[:,x:]=0
  if a==3:
    M[:y,:]=0
  if a==4:
    M[y:,:]=0
  #print(M)
print(int(M.sum()))