import sys
input = lambda: sys.stdin.readline().rstrip()

A, B, C = map(int, input().split())

print(A*B//2)