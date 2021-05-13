def gcd(x, y):
    if y == 0:
        print(x)
        return x
    return gcd(y, x%y)

x, y = map(int, input().split())
if y > x:
    t = y
    y = x
    x = t
gcd(x, y)