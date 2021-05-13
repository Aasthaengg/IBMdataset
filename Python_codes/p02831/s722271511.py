#!/usr/bin/python3

import sys
#import math
import fractions as math

def input():
    return sys.stdin.readline().rstrip('\n')

#N = int(input())
A,B = list(map(int, input().split()))

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

print(lcm(A,B))
