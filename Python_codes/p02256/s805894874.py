def gcd(x, y):
    if y == 0:
        return print(x)
    return gcd(y, x % y)

x, y = map(int, input().split())
gcd(x, y)
