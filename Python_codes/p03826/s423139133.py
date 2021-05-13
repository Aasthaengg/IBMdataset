import sys
input = sys.stdin.readline
A, B, C, D = [int(x) for x in input().split()]
print(max(A * B, C * D))