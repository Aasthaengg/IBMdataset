import fractions
a,b,c,d=map(int,input().split())
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)
e=lcm(c,d)
cc=b//c-(a-1)//c
dd=b//d-(a-1)//d
ee=b//e-(a-1)//e
print(b-a-cc-dd+ee+1)