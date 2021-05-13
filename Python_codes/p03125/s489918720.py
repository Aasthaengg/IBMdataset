import sys
input = lambda: sys.stdin.readline().rstrip()

A, B = map(int, input().split())


if B % A == 0:
    print(A+B)
else:
    print(B-A)