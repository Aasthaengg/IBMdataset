import math
n,a,b=map(int,input().split())
x=list(map(int,input().split()))
x.sort()
x.reverse()

j=a+1
moto=0
h=0
d=x[a-1]
asd=0
l=x.count(d)
for i in range(a):
  moto+=x[i]
  if x[i]==x[a-1]:
    h+=1
print(moto/a)
if moto/a==x[a-1]:
  for i in range(a,b+1):
    if l-i>=0:
      asd+=math.factorial(l)//(math.factorial(l-i)*math.factorial(i))
  print(asd)
else:
  print(math.factorial(l)//(math.factorial(l-h)*math.factorial(h))) 