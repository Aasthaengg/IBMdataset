import sys
input = sys.stdin.readline

a, b, c = [int(x) for x in input().split()]

a_ = a - b

transfer = min(a_, c)

print(c - transfer)