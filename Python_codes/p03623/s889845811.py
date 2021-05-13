import sys

x, a, b = map(int, sys.stdin.readline().split())

if abs(x-a) > abs(x-b):
    print("B")
else:
    print("A")