import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
inf = 10**18

N = int(input())
xmax = -inf
xmin = inf
ymax = -inf
ymin = inf
for _ in range(N):
    a, b = map(int, input().split())
    x = a + b
    y = a - b
    xmax = max(xmax, x)
    xmin = min(xmin, x)
    ymax = max(ymax, y)
    ymin = min(ymin, y)

print(max(xmax-xmin, ymax-ymin))