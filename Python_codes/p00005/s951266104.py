def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

while True:
    try:
        a,b = map(int, raw_input().split())
        c = gcd(a, b)
        print "{0} {1}".format(c, a*b/c)
    except:
        break