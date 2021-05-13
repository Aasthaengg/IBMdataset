import math

bl=input().split()
n=int(bl[0])
s=int(bl[1])

for a in range(math.ceil(s/2)):
  print(str(a+1)+" "+str(s-a+1))
for b in range(math.floor(s/2)):
  print(str(s+b+2)+" "+str(2*s-b+1))