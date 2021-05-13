# This program computes GCD and LCM
# -*- coding: utf-8
import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    for i in range(max([a, b]), a*b + 1):
        if(i % a == 0 and i % b == 0):
            return i
    return a*b


for i in sys.stdin:
    try:
        line = [int(k) for k in i.split(" ")]
        g = gcd(min(line), max(line))
        print(str(g) + " " + str(line[0]*line[1]//g))  # + str(lcm(line[0], line[1]))
    except:
        exit()