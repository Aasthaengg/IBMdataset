import math
A,B,C,D = map(int,input().split())
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

E = B//C + (-A//C) + 1
F = B//D + (-A//D) + 1
G = B//lcm(C,D) + (-A//lcm(C,D)) + 1
H = E + F - G
print(B - A + 1 - H)