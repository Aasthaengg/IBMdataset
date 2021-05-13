import sys
input = sys.stdin.readline
N, K = [int(x) for x in input().split()]
if N % K != 0:
    print(1)
else:
    print(0)