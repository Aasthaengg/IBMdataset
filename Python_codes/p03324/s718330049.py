import numpy as np
 
d,n = map(int, input().split())
if(not(n==100)):
  if(d==0):
    print(n)
  elif(d==1):
    print(100*n)
  else:
    print(10000*n)
else:
  if(d==0):
    print(101)
  elif(d==1):
    print(10100)
  else:
    print(1010000)