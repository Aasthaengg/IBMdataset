import math
n,k=map(int,input().split())
s=0
mi=math.inf
for i in range(n):
  a=int(input())
  rem=0
  s+=a
  if a<mi:
    mi=a 
  rem=k-s
if rem>0:
  res=rem/mi     
  print(int(res+n))
else:
  print(n)