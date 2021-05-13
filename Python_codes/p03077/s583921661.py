import math
n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=min(a,min(b,min(c,min(d,e))))
i=math.ceil(n/k)
while i*k<n:
  i+=1
print(4+i)
