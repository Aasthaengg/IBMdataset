def gcd(x,y):
    while y > 0:
        r = x % y
        x = y
        y = r
    return x

x,y = map(int,input().split())
print(gcd(x,y))
