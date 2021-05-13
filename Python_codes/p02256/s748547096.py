#Greatest Common Diveser
def gcd(a, b):
    while a > 0:
        if a < b: a, b = b, a
        a = a % b
    return b

x, y = map(int, input().split())
print(gcd(x, y))