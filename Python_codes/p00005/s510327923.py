#coding:utf-8

import sys

def gcd(n):
    x = n[0]
    y = n[1]

    while y:
        x, y = y, x % y

    return x


def lcm(n):
    return int(n[0] * n[1] / gcd(n))


if __name__ == '__main__':

    lines = []

    for line in sys.stdin:
        if line == "\n":
            break
        else :
            lines.append([int(item) for item in line.split(" ")])

    for n in lines:
        print(str(gcd(n)) + " " + str(lcm(n))) 