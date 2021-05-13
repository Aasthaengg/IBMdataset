import sys
A, B = map(int, sys.stdin.readline().rstrip().split())
if B % A == 0:
    print(A + B)
else:
    print(B - A)