
def gcd(a, b):
    if b>a:
        b, a = a, b

    d = 1
    while True:
        d = a % b
        if d == 0:
            break
        a, b = b, d

    return b


a, b = map(int, input().split())
print(gcd(a, b))