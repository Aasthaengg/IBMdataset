while True:
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a%b)
    def lcm(a, b):
        return a*b/gcd(a, b)

    try:
        a, b = map(int, input().split())
    except EOFError:
        break
    print(str(gcd(b, a%b)) + " " + str(int(lcm(a, b))))
