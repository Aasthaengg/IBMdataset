import sys

[A, B, C] = [int(x) for x in sys.stdin.readline().strip().split(" ")]

print(max(C - (A - B), 0))
