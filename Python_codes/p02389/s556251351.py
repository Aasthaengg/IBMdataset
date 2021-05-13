import sys

a, b = map(int, sys.stdin.readline().split())
print("%d %d" % (a * b, 2*a + 2*b))