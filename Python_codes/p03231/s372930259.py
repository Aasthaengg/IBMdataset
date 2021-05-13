n,m=map(int,input().split())
s=input()
t=input()
import fractions
g=fractions.gcd(n,m)
m0=m//g
n0=n//g
i=0
while i*n0<n and i*m0<m:
  if s[i*n0]==t[i*m0]:
    pass
  else:
    print(-1)
    exit()
  i+=1
print(n*m//g)
