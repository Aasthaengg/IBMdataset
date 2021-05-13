import sys
input = sys.stdin.readline
from collections import *

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a//gcd(a, b)*b

A, B = map(int, input().split())
print(lcm(A, B))