def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
while True:
    try:
        a, b = map(int, input().split())
        d = gcd(max(a, b), min(a, b))
        print(d, a * b // d)
    except:
        break