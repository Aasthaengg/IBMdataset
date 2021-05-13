# Aizu Problem ITP_1_10_D: Distance II
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


n = int(input())
X = [int(_) for _ in input().split()]
Y = [int(_) for _ in input().split()]
for p in range(1, 4):
    D = 0
    for i in range(n):
        D += pow(abs(X[i] - Y[i]), p)
    D = pow(D, 1 / p)
    print("%.6f" % D)
D = 0
for i in range(n):
    D = max(D, abs(X[i] - Y[i]))
print("%.6f" % D)