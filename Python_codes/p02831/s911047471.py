import fractions
a,b = map(int, input().split())
def lcm(x,y):
    return x*y / fractions.gcd(x,y)
print(int(lcm(a,b)))