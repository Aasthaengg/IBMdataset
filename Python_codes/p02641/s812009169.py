import numpy as np
X,N=map(int,input().split())


    
if N==0:
	print(X)
else:
  p=list(map(int,input().split()))
  p=sorted(p)
  if X in p:
      s=X-1
      t=X+1
      while True:
          if s not in p:
              print(s)
              break
          elif t not in p:
              print(t)
              break
          else:
              s=s-1
              t=t+1
  else:
      print(X)
