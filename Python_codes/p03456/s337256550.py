import math
a,b=input().split()
n=a+b
n=int(n)
if int(math.sqrt(n))**2==n:
  print("Yes")
else:
  print("No")