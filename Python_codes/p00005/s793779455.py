# Aizu Problem 0006: GCD and LCM
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


def gcd(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


for line in sys.stdin:
    a, b = [int(_) for _ in line.split()]
    print(gcd(a, b), lcm(a, b))