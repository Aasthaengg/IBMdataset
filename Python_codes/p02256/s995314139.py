
def gcd(x, y):

    if y > x:
        x, y = y, x

    if y == 0:
        return x

    if x >= y:
        return gcd(y, x % y)


x, y = [int(i) for i in input().split()]
print(gcd(x, y))