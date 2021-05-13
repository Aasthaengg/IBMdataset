import sys
a, b, c, k = [int(i) for i in sys.stdin.readline().split()]
print((a - b) * (-1) ** k)