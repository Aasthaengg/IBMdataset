n=int(input())
 
a=2
b=1
s=0
 
if n==1:
  s=1
  n=2
 
for i in range(n-1):
  nn = a+b
  ans=nn
  a=b
  b=nn
 
if s==1:
  ans = 1
 
print(ans)