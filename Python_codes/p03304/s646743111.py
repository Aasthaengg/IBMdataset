import sys
input = sys.stdin.readline
N, M, D = map(float, input().split())
print((M - 1) / N + ((N - 2 * D) > 0 and (D > 0)) * (N - 2 * D) * (M - 1) / (N ** 2))