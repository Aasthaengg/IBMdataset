def gcd(x,y):
    while y:
        x, y = y, x % y
    return x

a,b = map(int, raw_input().split())
print gcd(a, b)
