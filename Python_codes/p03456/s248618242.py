import sys
 
A,B=input().split()
X=int(A+B)
L=[x*x for x in range(1,1001)]
 
if X in L:
  print('Yes')
else:
  print('No')