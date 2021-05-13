import sys
input = sys.stdin.readline
a = [int(x) for x in input().split()]
a.sort()
print(a[0] + a[1])