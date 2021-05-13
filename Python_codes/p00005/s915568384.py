def gcd(x, y):
    if x > y:
        x, y = y, x
    while x > 0:
        x, y = y%x, x
    return y

def lcm(x, y):
    z = gcd(x, y)
    return x*y//z

if __name__ == "__main__":
    while True:
        try:
            a, b = map(int, input().split())
            g = gcd(a, b)
            l = lcm(a, b)
            print("{} {}".format(g, l))
        except:
            break

