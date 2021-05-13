import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

dis = INF
ans = None
for i, h in enumerate(H):
    avg = T - h * 0.006
    if abs(avg - A) < dis:
        dis = abs(avg - A)
        ans = i + 1
print(ans)