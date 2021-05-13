from collections import defaultdict, Counter
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

H, W, N = map(int, input().split())
d = defaultdict(int)
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(-2, 1):
        if 1 <= x + i <= H - 2:
            for j in range(-2, 1):
                if 1 <= y + j <= W - 2:
                    d[(x + i, y + j)] += 1

c = Counter(d.values())
zero = (H - 2) * (W - 2) - len(d)
print(zero)
for i in range(1, 10):
    print(c[i])