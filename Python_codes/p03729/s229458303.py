import sys
input = sys.stdin.readline

A,B,C = list(input().rstrip().split())
print('YES' if A[-1]==B[0] and B[-1]==C[0] else 'NO')
