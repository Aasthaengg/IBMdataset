import sys
input = sys.stdin.readline

h, w, d = [int(x) for x in input().split()]
n = h*w
a = [[int(x) for x in input().split()] for _ in range(h)]
q = int(input())
lr = [[int(x) for x in input().split()] for _ in range(q)]

from collections import defaultdict
b = defaultdict(list)
for i in range(h):
    for j in range(w):
        b[a[i][j] - 1] = [i, j]
dist = [float('inf')]*n
for i in range(d):
    dist[i] = 0
    while i + d < n:
        x1, y1 = b[i]
        x2, y2 = b[i + d]
        dist[i + d] = dist[i] + abs(x1 - x2) + abs(y1 - y2)
        i += d
for i in range(q):
    l, r = lr[i]
    l -= 1
    r -= 1
    print(dist[r] - dist[l])