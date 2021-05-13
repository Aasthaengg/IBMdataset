import math
def distance(x,y):
  return math.sqrt(x**2+y**2)

n,d=input().split()
n=int(n)
d=int(d)
count=0
for i in range(n):
  x,y=input().split()
  x=int(x)
  y=int(y)
  r=distance(x,y)
  if(r<=d):
    count+=1

print(count)