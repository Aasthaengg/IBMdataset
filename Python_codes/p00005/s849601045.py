import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)

def calc(a, b):
    gcd_val = gcd(a, b)
    lcm_val = a * b / gcd_val
    return (gcd_val, lcm_val)


for line in sys.stdin.readlines():
    line = line.strip()
    a, b = map(int, line.split())
    print "{0[0]:d} {0[1]:d}".format(calc(a, b))