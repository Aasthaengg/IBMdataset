def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a,b)


while True:
    try:
        a, b = [int(i) for i in input().split()]
        print(gcd(a, b), lcm(a, b))
    except EOFError:
        break