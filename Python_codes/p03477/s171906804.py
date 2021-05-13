import sys
input = sys.stdin.readline
A, B, C, D = [int(x) for x in input().split()]
if (A + B) > (C + D):
    print("Left")
elif (A + B) < (C + D):
    print("Right")
else:
    print("Balanced")