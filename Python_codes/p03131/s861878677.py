k,a,b=map(int,input().split())
import sys

if k<a-1 or b-a <2:
  print(k+1)
  sys.exit()
if (k+1-a) %2 ==0:
  print(a+(b-a)*(k+1-a)//2)
else:
  print(a+(b-a)*((k-a)//2)+1)    
