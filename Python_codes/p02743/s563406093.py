A,B,C=map(int,input().split())
if(4*A*B<(C-A-B)**2 and C-A-B>0):
  print("Yes")
else:
  print("No")
