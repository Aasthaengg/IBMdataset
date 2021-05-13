import sys

N, a, b = list(map(int, sys.stdin.readline().strip().split(" ")))

interval = max(a, b) - min(a, b) - 1

if interval % 2 == 0:
    print("Borys")
if interval % 2 == 1:
    print("Alice")