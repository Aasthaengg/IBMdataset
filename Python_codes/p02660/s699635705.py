from math import sqrt
n=int(input())
t=0
i=2
while i*i<=n:
  if n%i==0:
    c=0
    while n%i==0:
      n//=i
      c+=1
    t+=(int(sqrt(8*c+1))-1)//2
  i+=1
if n>1:
  t+=1
print(t)