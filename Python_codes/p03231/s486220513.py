from math import gcd
 
n,m=map(int, input().split())
s=input()
t=input()
 
g=gcd(n,m)
 
ng=n//g
mg=m//g
 
for i in range(0,g):
    if s[ng*i]!=t[mg*i]:
        print(-1)
        exit()
print(ng*mg*g)