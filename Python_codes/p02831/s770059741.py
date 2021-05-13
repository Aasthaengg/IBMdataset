a,b = list(map(int,input().split()))
import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

l = lcm(a, b)
print(min(l,a*b))