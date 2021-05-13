import sys

N, D = map(int, sys.stdin.readline().split())
print((N - 1)// (2*D+1) + 1)