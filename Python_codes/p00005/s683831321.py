
def gcd(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)

def lcm(a, b, g):
    return a * b / g
    

while True:
    try:
        a, b = map(int, raw_input().split())
    except EOFError:
        break

    g = gcd(a, b) 
    print "{} {}".format(g, lcm(a,b,g)) 