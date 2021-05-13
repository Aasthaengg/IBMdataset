import sys
import math

inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

a, b, c, d = inintm()

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

print(b - (b//c + b//d) + b//lcm(c,d) - ((a-1) - ((a-1)//c + (a-1)//d) + (a-1)//lcm(c,d)))
