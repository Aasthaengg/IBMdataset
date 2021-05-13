import sys
input = sys.stdin.readline

a, p = [int(x) for x in input().split()]
p += 3*a
print(p//2)
