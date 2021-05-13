import math

if __name__ == '__main__':
    a, b, C = [int(i) for i in input().split()]
    theta = math.radians(C)
    S = a * b * math.sin(theta) / 2
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(theta))
    L = a + b + c
    h = b * math.sin(theta)
    [print("{0:.5f}".format(i)) for i in [S, L, h]]