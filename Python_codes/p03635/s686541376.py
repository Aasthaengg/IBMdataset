import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
print((m - 1)*(n - 1))