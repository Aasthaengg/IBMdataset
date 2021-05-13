def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

while True:
    try:
        a, b = map(int, raw_input().split())
        print gcd(a, b), a*b/ gcd(a,b)
    except:
        break
