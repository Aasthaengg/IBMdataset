def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def lcm(a,b,g):
    return a*b/g

while 1:
    try:
        a,b=map(int,raw_input().split())
        g=gcd(a,b)
        print g,lcm(a,b,g)
    except:
        break