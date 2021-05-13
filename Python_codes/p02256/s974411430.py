def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        x, y = y, x%y
    return x

x, y = list(map(int, input().split()))
print(gcd(x, y))

