import sys
x,y=map(int,input().split())
MOD=10**9+7
if (2*y-x)%3!=0 or 2*y-x<0 or 2*x-y<0:
  print(0)
  sys.exit()
a=(2*x-y)//3
if (a+1)*3<=(2*x-y):
  a+=1
a=(2*x-y)//3
if (a+1)*3<=(2*x-y):
  a+=1
b=(2*y-x)//3
if (b+1)*3<=(2*y-x):
  b+=1
p=1
for i in range(1,a+b+1):
  p=(p*i)%MOD
q=1
for i in range(1,a+1):
  q=(q*i)%MOD
q=pow(q,MOD-2,MOD)
r=1
for i in range(1,b+1):
  r=(r*i)%MOD
r=pow(r,MOD-2,MOD)
print((p*q*r)%MOD)
