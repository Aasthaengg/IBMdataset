import math
a,b,c,d = map(int, input().split())

C = b//c - (a-1)//c
D = b//d - (a-1)//d
x = c*d//math.gcd(c,d)
CD = b//x - (a-1)//x

print((b-a+1) - (C+D-CD))