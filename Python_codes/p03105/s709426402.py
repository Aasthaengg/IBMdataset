import sys
input = sys.stdin.readline

a, b, c = [int(x) for x in input().split()]
print(min(b//a, c))