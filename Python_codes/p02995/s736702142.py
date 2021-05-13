def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return a*b // gcd(a,b)

a,b,c,d = map(int,input().split())
a -= 1
A = a-((a//c) + (a//d) - a//lcm(c,d))
B = b-((b//c) + (b//d) - b//lcm(c,d))
print(B-A)