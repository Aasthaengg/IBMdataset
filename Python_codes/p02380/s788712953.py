# coding=utf-8
from math import sin, pi, sqrt, cos


def main():
    a, b, CinDeg = map(int, raw_input().split())
    CinRad = pi * CinDeg / 180
    S = 0.5 * a * b * sin(CinRad)
    c = sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(CinRad))
    L = a + b + c
    h = S / (0.5 * a)
    print S
    print L
    print h

if __name__ == '__main__':
    main()