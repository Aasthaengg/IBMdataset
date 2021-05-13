def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return (a*b)//gcd(a,b)

while True:
    try:
        a,b=map(int,input().split())
    except:
        break
    print(gcd(a,b),lcm(a,b))
