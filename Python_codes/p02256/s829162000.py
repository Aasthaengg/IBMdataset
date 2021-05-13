def gcd(x, y):
    while x > 0:
        x, y = y % x, x
    return y


xy = list(map(int, input().split()))
x = xy[0]
y = xy[1]
y = gcd(x, y)
print(y)
