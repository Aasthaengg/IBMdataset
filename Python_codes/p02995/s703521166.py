import math
a,b,c,d=map(int,input().split())
count=b-a+1
acou=((a-1)//c)+((a-1)//d)-int(((a-1)//(c*d//math.gcd(c,d))))
bcou=(b//c)+(b//d)-int((b//(c*d//math.gcd(c,d))))
print(count-(bcou-acou))
