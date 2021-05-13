from  math import log,floor
n=int(input())

if n==0:
  print(0)
  exit(0)

if n%2==1:
  print(0)
  exit(0)

f=floor(log(n,5))
ans=0
for i in range(f):
  t=n//(5**(f-i))
  ans+=t//2
print(ans)

