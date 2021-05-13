import sys

a, b, c = map(int, sys.stdin.readline().split())

m = max([a,b,c])

print(a + b + c - m)