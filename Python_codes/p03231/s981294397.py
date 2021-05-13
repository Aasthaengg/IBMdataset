import fractions
n,m=map(int,input().split())
s=input()
t=input()
a=fractions.gcd(n,m)
if s[::n//a] == t[::m//a]:
  print(n*m//a)
else:
  print(-1)