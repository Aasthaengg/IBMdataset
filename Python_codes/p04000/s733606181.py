# O(N)
import collections
H, W, N = map(int, input().split())
table = collections.defaultdict(int) # (left, top) of 3x3 block => black count
for i in range(N):
    a, b = map(int, input().split())
    for yy in range(3):
        for xx in range(3):
            y = a - 1 - yy
            x = b - 1 - xx
            if 0 <= y and y + 2 < H and 0 <= x and x + 2 < W:
                table[(y, x)] += 1
counts = [0] * 10
for v in table.values():
    counts[v] += 1
counts[0] = (H - 2) * (W - 2) - sum(counts)
for c in counts:
    print(c)
