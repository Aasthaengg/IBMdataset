import fractions
x,y=map(int,input().split())
a=x*y/fractions.gcd(x,y)
a-=x
if a>0 and a<10**19:
     print(int(a))
else:
     print(-1)