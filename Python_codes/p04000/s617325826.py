import sys
from itertools import product
from collections import Counter
input = sys.stdin.readline

H, W, N = map(int, input().split())
udlr = [-1, 0, 1]
center = []

for _ in range(N):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    for i, j in product(udlr, repeat=2):
        if 0 < a + i < H - 1 and 0 < b + j < W - 1:
            center.append((a + i, b + j))

black = Counter(list(Counter(center).values()))
black[0] = (H - 2) * (W - 2) - sum(list(black.values()))

for i in range(10):
    if black.get(i):
        print(black[i])
    else:
        print(0)