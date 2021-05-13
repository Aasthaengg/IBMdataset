import math
n,p=map(int,input().split())
c=0
for m in map(int,input().split()):
  if m%2==0:c+=1
d=2**(c)

e=0
for i in range(p,n-c+1,2):
  
  k=math.factorial(n-c) // (math.factorial(n-c - i) * math.factorial(i))
  k=max(k,1)
  e+=k

print(d*e)
