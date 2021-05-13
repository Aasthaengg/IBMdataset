import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

A, B, C, K = map(int, input().split())

if K % 2 == 0:
    ans = A - B
else:
    ans = B - A

print(ans)