import sys
import math


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

a,b=inintm()

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

print(lcm(a,b))
