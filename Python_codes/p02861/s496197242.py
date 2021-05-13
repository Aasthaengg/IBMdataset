n=int(input())
x=[]
y=[]
for i in range(n):
  a,b=map(int,input().split())
  x.append(a)
  y.append(b)
ans=0
import math
for i in range(n):
  for j in range(n):
    ans+=math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
ans=ans/(n*(n-1))
print(ans*(n-1))