from math import gcd
n,m=map(int,input().split())
s=input()
t=input()
res=n*m//gcd(n,m)
a=m//gcd(n,m)
b=n//gcd(n,m)
if n>=m:
  for i in range(m):
    if (i*b)%a==0:
      if s[(i*b)//a]!=t[i]:
        print(-1)
        exit()
else:
  for i in range(n):
    if (i*a)%b==0:
      if s[i]!=t[(i*a)//b]:
        print(-1)
        exit()
print(res)