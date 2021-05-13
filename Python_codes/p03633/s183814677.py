from math import gcd

N = int(input())
t = [int(input()) for i in range(N)]

def lcm(t):
    x = t[0]
    for i in range(1, len(t)):
        x = (x * t[i]) // gcd(x, t[i])
    return x

print(lcm(t))

