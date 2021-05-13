def gcd(a, b):
    """a, bの最大公約数(greatest common divisor:GCD)を求める"""
    if b == 0:
        return a
    return gcd(b, a%b)


a, b = map(int,input().split())
gcd_ab = gcd(a, b)
if gcd_ab == b:
    print(-1)
else:
    if a % b == 0:
        print(a*gcd_ab)
    else:
        print(a)