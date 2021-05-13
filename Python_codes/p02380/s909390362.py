import math


def main():
    a, b, c = map(int, input().split())
    angle = math.radians(c)
    s = (1/2) * math.sin(angle) * a * b
    L = a + b + (a**2 + b**2 - 2*a*b*math.cos(angle))**(1/2)
    h = math.sin(angle) * b
    print('{0:.5f}\n{1:.5f}\n{2:.5f}'.format(s, L, h))


if __name__ == '__main__':
    main()

