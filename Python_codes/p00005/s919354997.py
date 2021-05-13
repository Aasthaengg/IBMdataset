# This program computes GCD and LCM
# -*- coding: utf-8
import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


for i in sys.stdin:
    try:
        line = [int(k) for k in i.split(" ")]
        g = gcd(min(line), max(line))
        print(str(g) + " " + str(line[0]*line[1]//g))
    except:
        exit()