import sys

a, b, c, d = map(int, sys.stdin.readline().split())

if abs(a-c) <= d or (abs(a-b) <= d and abs(c-b) <= d):
    print("Yes")
else:
    print("No")