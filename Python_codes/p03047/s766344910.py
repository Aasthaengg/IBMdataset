import sys
input = sys.stdin.readline

N, K = [int(x) for x in input().split()]

print(N-K+1)
