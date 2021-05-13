a,b=map(int, input().split())

def gcd(l,s):
    r = l%s
    if r == 0:
        return s
    else:
        return gcd(s,r)

def lcm(x,y):
    return (x * y) // gcd(x, y)

print(lcm(a,b))