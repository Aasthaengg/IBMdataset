import math
N=int(input())
a=int((math.sqrt(N)//1))
ans=0
if N==2:
  print(0)
  exit()
for i in range(1,a):
  b=(N-i)/i
  if b.is_integer():
    ans+=int(b)
c=N//a
d=N%a
if int(c)==d:
  ans+=a
a+=1
c=N//a
d=N%a
if int(c)==d:
  ans+=a
print(ans)