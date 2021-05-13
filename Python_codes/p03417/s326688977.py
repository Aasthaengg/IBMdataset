import sys
input = sys.stdin.readline
N,M = [int(i) for i in input().split()]
print(abs((N-2) * (M-2)))