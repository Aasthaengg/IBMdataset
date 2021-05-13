import sys
sys.setrecursionlimit(5 * 10**5)
input = sys.stdin.readline

N, M = list(map(int, input().split()))

A = 1 - 1 / 2**M
B = 100 * N + 1800 * M

ans = A * B / (2**M - 1) / (1 - A)**2

print(round(ans))