import sys
input = sys.stdin.readline
X, t = [int(x) for x in input().split()]
print(max(0, X - t))