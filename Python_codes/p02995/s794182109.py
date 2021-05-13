import math
l = list(map(int,input().split()))

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

l[0] -= 1
la = l[0] - l[0] // l[2] - l[0] // l[3] + l[0] // lcm(l[2], l[3])
lb = l[1] - l[1] // l[2] - l[1] // l[3] + l[1] // lcm(l[2], l[3])
print(lb - la)