import math
n=int(input())
c=[]
for i in range(n):
  x,y=[int(x) for x in input().split()]
  c.append([x,y])
d=0
for i in range(n-1):
  for j in range(i+1,n):
    d+=math.sqrt((c[i][0]-c[j][0])**2+(c[i][1]-c[j][1])**2)
print(2*d/n)