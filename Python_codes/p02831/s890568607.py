def gcd(a,b):
    if not a%b:
        return b
    return gcd(b,a%b)
a,b = map(int, input().split())
print(a*b//gcd(max(a,b),min(a,b)))