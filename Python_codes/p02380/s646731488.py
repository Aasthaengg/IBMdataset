# Aizu Problem ITP_1_10_B: Triangle
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


a, b, C = [int(_) for _ in input().split()]
C *= math.pi / 180
S = a * b * math.sin(C) / 2
c = math.sqrt(a**2 - 2 * a * b * math.cos(C) + b**2)
L = a + b + c
h = 2 * S / a
print("%.8f\n%.8f\n%.8f" % (S, L, h))