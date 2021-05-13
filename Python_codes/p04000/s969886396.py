import collections

h, w, n = map(int, input().split())
squares = collections.defaultdict(lambda: collections.defaultdict(int))
for index in range(n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    for i in range(-2, 1):
        for j in range(-2, 1):
            y = a + i
            x = b + j
            if 0 <= x < w - 2 and 0 <= y < h - 2:
                squares[y][x] += 1
counter = collections.Counter()
for y, xs in squares.items():
    for x, count in xs.items():
        counter[count] += 1
print((h - 2) * (w - 2) - sum(counter.values()))
for i in range(1, 10):
    print(counter[i])