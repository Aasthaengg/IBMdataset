import numpy as np

W,H,N = map(int,input().split())
l = np.zeros((H,W)) #	要素0のH×W配列

for i in range(N):
  x,y,a = map(int,input().split())

  if a==1:
    l[:,:x] = 1
    #print(l[:,x:])
  elif a==2:
    l[:,x:] = 1
  elif a==3:
    l[:y,:] = 1
  elif a==4:
    l[y:,:] = 1
#print(H*W-int(l.sum().sum()))
print(H*W-int(l.sum()))