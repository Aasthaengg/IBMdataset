def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

x,y=map(int,raw_input().split())
print(gcd(x,y))