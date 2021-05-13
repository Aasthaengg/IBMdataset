import sys

N,K = map(int,sys.stdin.readline().rstrip().split())

print(0 if N % K == 0 else 1)