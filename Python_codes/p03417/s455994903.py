from sys import stdin

N, M = map(int, stdin.readline().split())

print(abs(N * M - 2 * (N + M) + 4))
