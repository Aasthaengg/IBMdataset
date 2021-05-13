n,m=map(int,input().split())
s=input()
t=input()
import fractions
x=n*m//(fractions.gcd(n,m))
n1=x//n
m1=x//m
x1=n1*m1//(fractions.gcd(n1,m1))
if n%m==0:
  for i in range(m):
    if t[i]!=s[n*i//m]:
      print("-1")
      exit()
  print(x)
  exit()
elif m%n==0:
  for i in range(n):
    if s[i]!=t[m*i//n]:
      print("-1")
      exit()
  print(x)
  exit()
else:
  for i in range(x//x1):
    if s[i*x1//n1]!=t[i*x1//m1]:
      print(-1)
      exit()
print(x)