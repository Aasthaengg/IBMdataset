# Aizu Problem ITP_1_3_D: How Many Divisors?
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


a, b, c = [int(_) for _ in input().split()]
print(sum([c % k == 0 for k in range(a, b + 1)]))