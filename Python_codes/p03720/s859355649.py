import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N, M = map(int, input().split())
l = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    l[a-1] += 1
    l[b-1] += 1

print(*l, sep="\n")