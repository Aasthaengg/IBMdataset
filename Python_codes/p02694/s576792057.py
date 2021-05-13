import math
n=int(input())
c=100
for i in range(4000):
  c=(c*101)//100
  if c>=n:
    print(i+1)
    break