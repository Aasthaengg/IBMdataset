import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N, K = map(int, input().split())
H = []
for _ in range(N):
    H.append(int(input()))
H.sort()

ans = INF
for i in range(N-K+1):
    ans = min(ans, H[i+K-1] - H[i])

print(ans)