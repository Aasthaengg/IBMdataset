import sys
for i in sys.stdin:
    a,b=map(int,i.split())
    if a<b:a,b=b,a
    def gcd(x,y):
        while y>0:x,y=y,x%y
        return x
    def lcm(x,y):
         return x*y/gcd(x,y)
    print(gcd(a,b),int(lcm(a,b)))