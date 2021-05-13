import sys
input = sys.stdin.readline
from collections import *
from fractions import *

def lcm(a, b):
    return a*b//gcd(a, b)

N = int(input())
L = 1

for _ in range(N):
    T = int(input())
    L = lcm(L, T)

print(L)