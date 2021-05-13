n, m=map(int, input().split())
S=input()
T=input()

if n==1 and m==1:
  if S==T:
    print(1)
  else:
    print(-1)
  exit()
elif n==1 or m==1:
  print(-1)
  exit()

import fractions
p=n*m//fractions.gcd(n, m)
a=p//n
b=p//m
c=a*b//fractions.gcd(a, b)
for i in range(0, p, c):
  if S[i//a]!=T[i//b]:
    print(-1)
    exit()
    
print(p)