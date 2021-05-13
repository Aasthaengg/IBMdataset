from math import gcd
def lcm(a, b):
    return a*b//gcd(a,b)

A, B, C, D = map(int,input().split())

nC = B//C - -(-A//C) + 1
nD = B//D - -(-A//D) + 1
nCD = B//lcm(C,D) - -(-A//lcm(C,D)) + 1

print((B-A+1)-(nC+nD-nCD))