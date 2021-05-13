#!/usr/bin/env python3

import math
import sys


def dist():
    coordinates = [float(num) for num in sys.stdin.readline().split()]
    return math.hypot(coordinates[2]-coordinates[0],
                      coordinates[3]-coordinates[1])


def main():
    print(dist())


if __name__ == '__main__':
    main()