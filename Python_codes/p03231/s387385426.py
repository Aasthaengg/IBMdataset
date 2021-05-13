from fractions import gcd
n,m=map(int,input().split())
s=input()
t=input()
g=gcd(n,m)
l=n*m//g
for i in range(n):
  if i%(n//g)==0 and not s[i]==t[i*m//n]:
    print(-1)
    exit()
print(l)