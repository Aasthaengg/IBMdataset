import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

x1, y1, x2, y2 = map(int, input().split())

x = x2 - x1
y = y2 - y1

print(x2 - y, y2 + x, x1 - y, y1 + x)