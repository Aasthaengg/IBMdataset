import math
n=int(input())
for i in range(n,0,-1):
  if math.sqrt(i)%1==0:
    print(i)
    exit()
