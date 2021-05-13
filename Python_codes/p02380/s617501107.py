#
# 10b
#
import math


def main():
    a, b, C, = map(float, input().split())
    d = math.radians(C)
    h = math.sin(d) * b
    S = a * h / 2
    L = a + b + math.sqrt(a**2+b**2-2*a*b*math.cos(d))
    print(f"{S: .4f}")
    print(f"{L: .4f}")
    print(f"{h: .4f}")


if __name__ == '__main__':
    main()
