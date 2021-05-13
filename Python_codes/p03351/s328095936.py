import sys
input = sys.stdin.readline
a, b, c, d = [int(x) for x in input().split()]
if abs(c - a) <= d or (abs(b - a) <= d and abs(c - b) <= d):
    print("Yes")
else:
    print("No") 