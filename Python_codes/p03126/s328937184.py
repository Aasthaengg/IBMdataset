import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N, M = map(int, input().split())
suki = [0] * M
for _ in range(N):
    K, *A = map(int, input().split())
    for a in A:
        suki[a-1] += 1

ans = len(list(filter(lambda x: x == N, suki)))
print(ans)
