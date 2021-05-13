import sys
readline = sys.stdin.readline

N, K = map(int, readline().split())
print(K*pow(K-1, N-1))