from collections import *
n=int(input())
x=[0]*n
y=[0]*n
for i in range(n):
  x[i],y[i]=map(int,input().split())
a=[]
for i in range(n):
  for j in range(n):
    if i==j:continue
    a+=[(x[i]-x[j],y[i]-y[j])]
c=list(Counter(a).values())
print(n-max(c) if c else n)