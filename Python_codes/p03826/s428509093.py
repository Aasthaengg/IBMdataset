import sys

a,b,c,d = map(int, sys.stdin.readline().split())

print(max(a * b, c * d))