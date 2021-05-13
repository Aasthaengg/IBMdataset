import sys

readline = sys.stdin.readline

N, K = map(int, readline().split())

if K == 1:
    print(0)
else:
    print(N - K)