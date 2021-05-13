import math
a, b, c=input().split(" ")
a = int(a) 
b = int(b)
c = int(c) 

if  4*a*b < (c-a-b)*(c-a-b) and (c-a-b)>0:
  print("Yes")
else:
  print("No")