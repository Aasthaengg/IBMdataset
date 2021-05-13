import sys
input = lambda : sys.stdin.readline().rstrip()

a, b = map(int, input().split())
print(max(0, a - 2*b))