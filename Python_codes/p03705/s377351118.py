import sys
input = sys.stdin.readline
N, A, B = map(int, input().split())
print(max(0, (N - 1) * B + A - ((N - 1) * A + B) + 1))