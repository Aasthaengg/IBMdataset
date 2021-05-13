import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N, M = map(int, input().split())
maxL = 1
minR = N
for _ in range(M):
    L, R = map(int, input().split())
    maxL = max(maxL, L)
    minR = min(minR, R)
ans = minR - maxL + 1
ans = max(ans, 0)
print(ans)