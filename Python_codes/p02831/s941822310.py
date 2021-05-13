a, b = map(int, input().split())


def gcd(a, b):
    if a > b:
        a, b = b, a
    while a > 0:
        a, b = b % a, a
    return b


def lcm(a, b):
    return (a * b) // gcd(a, b)


print(lcm(a, b))
