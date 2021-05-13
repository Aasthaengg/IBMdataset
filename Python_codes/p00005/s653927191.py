def gcd(a,b):
    r = a % b
    while r > 0:
        a = b
        b = r
        r = a % b
    return b

def lcm(a,b):
    return a*b / gcd(a,b)

while True:
    try:
        a,b = map(int, raw_input().split())
        print str(gcd(a,b)) + " " + str(lcm(a,b))
    except EOFError:
        break