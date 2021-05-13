# Aizu Problem ITP_1_10_C: Standard Deviation
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


while True:
    n = int(input())
    if n == 0:
        break
    A = [int(_) for _ in input().split()]
    mean = sum(A) / n
    sd = math.sqrt(sum([(a - mean)**2 for a in A]) / n)
    print("%.8f" % sd)