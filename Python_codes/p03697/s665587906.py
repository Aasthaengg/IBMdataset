import sys
input = sys.stdin.readline
A, B = [int(x) for x in input().split()]
if A + B >= 10:
    print("error")
else:
    print(A + B)
