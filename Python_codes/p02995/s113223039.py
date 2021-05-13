import math
a,b,c,d=map(int,input().split())
count=b-a+1

A=a-1
l=c*d//math.gcd(c,d)
acou=(A//c)+(A//d)-int((A//l))
bcou=(b//c)+(b//d)-int((b//l))

print(count-(bcou-acou))