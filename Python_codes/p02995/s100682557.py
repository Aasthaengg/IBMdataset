import math
def lcm(x,y):
    return (x*y)//math.gcd(x,y)
a,b,c,d=map(int,input().split())
bc=b//c
bd=b//d
bcd=b//lcm(c,d)
x=b-(bc+bd-bcd)
a=a-1
ac=a//c
ad=a//d
acd=a//lcm(c,d)
y=a-(ac+ad-acd)
print(x-y)