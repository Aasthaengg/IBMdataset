def gcd(a, b):
    if a<b:
        a,b = b,a
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b
a,b = map(int,input().split())
print(a * b // gcd(a, b))