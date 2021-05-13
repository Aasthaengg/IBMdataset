import math
n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=min(a,min(b,min(c,min(d,e))))
s=math.ceil(n/k)
while s*k<n:
  s+=1
print(5+s-1)