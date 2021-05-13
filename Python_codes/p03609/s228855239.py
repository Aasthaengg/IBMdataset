import sys

x, y = map(int, sys.stdin.readline().split())

print(max(0, x - y))