import sys
input = sys.stdin.readline
N, A, B = map(int, input().split())
print(min(N * A, B))