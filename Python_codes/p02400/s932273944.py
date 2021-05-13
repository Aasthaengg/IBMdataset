#!usr/bin/env python3

import sys
from math import pi


def area_of_circle(radius):
    return pi * radius**2


def circumference_of_circle(radius):
    return 2*pi*radius


def main():
    r = float(sys.stdin.readline())
    print('%f %f' % (area_of_circle(r), circumference_of_circle(r)))


if __name__ == '__main__':
    main()