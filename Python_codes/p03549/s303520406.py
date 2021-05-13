import sys
input = sys.stdin.readline
N, M = map(int, input().split())
t = pow(2, M)
print((M * 1900 + (N - M) * 100) * t)