import math

n=int(input())
a=int(input())

n=n-math.floor(n/500)*500
if n<=a:
  print("Yes")
  
else:
  print("No")