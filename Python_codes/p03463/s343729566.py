import sys
n, a, b = [int(i) for i in sys.stdin.readline().split()]
if (b - a - 1) % 2 == 1:
    print("Alice")
else:
    print("Borys")