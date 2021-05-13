# Aizu Problem ALDS_1_1_B: Greatest Common Divisor
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input2.txt", "rt")


def gcd(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a

x, y = [int(_) for _ in input().split()]
print(gcd(x, y))