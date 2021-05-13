import sys
input = sys.stdin.readline
A, B = [int(x) for x in input().split()]
if A + B >= 24:
    print(A + B -24)
else:
    print(A + B)