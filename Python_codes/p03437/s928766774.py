import math
x, y = map(int, input().split())
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(x,y):
    return (x * y)//gcd(x, y)

def thingo(x,y):
    if (x == 0 and y == 0):
        return -1
    if (x != 0 and y == 0):
        return x
    test = lcm(x,y)
    if (test-x >= x):
        return test-x
    else:
        return -1
print(thingo(x,y))
