import fractions
a,b,c,d=map(int, input().split())
ans = 0
f=fractions.gcd(c,d)
f2=c*d//f

bf = b//f2
af = (a-1)//f2

cb = b//c
ca = (a-1)//c

db = b//d
da = (a-1)//d

print(b-a+1-(cb-ca)-(db-da)+(bf-af))