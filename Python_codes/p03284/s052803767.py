import math
n,k=map(int,input().split())

if n%k==0:
  print(0)
else:
  max=math.floor(7/3)
  min=7%3
  print(max-min)