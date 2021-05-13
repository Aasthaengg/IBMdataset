def gcd(a, b):
    if a == 0: return b
    if b == 0: return a
    if a == b: return a
    if a > b: return gcd(b, a%b)
    return gcd(a, b%a)
def lcm(a, b):
    if a == b == 0:
        return 0
    return abs(a*b)/gcd(a, b)
a, b = map(int, input().split())
print(int(lcm(a, b)))
