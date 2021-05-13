import numpy as np
h,w=map(int,input().split())
field=[list(input()) for i in range(h)]
field=[[0 if field[j][i]=='#' else h+w for i in range(w)]for j in range(h)]
field=np.array(field)
for i in range(1,h):
  field[i,:]=np.minimum(field[i,:],field[i-1,:]+1)
for i in range(h-1,0,-1):
  field[i-1,:]=np.minimum(field[i,:]+1,field[i-1,:])
for i in range(1,w):
  field[:,i]=np.minimum(field[:,i],field[:,i-1]+1)
for i in range(w-1,0,-1):
  field[:,i-1]=np.minimum(field[:,i]+1,field[:,i-1])
print(np.max(field))