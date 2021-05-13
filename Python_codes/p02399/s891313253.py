import sys

a, b = map(int, sys.stdin.readline().split())
print("%d %d %f" % (a/b, a%b, a/b))