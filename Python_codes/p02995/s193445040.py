def lcm(x,y):
    return x*y//gcd(x,y)

def cnt(x):
    return B//x - A//x + (A%x==0)

from math import gcd

A, B, C, D = map(int, input().split())
l = lcm(C,D)

print((B-A+1)-cnt(C)-cnt(D)+cnt(l))