from collections import Counter

H, W, N, *AB = map(int, open(0).read().split())

move = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),  (0, 0),  (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

C = Counter()
for a, b in zip(*[iter(AB)] * 2):
    for i, j in move:
        if 2 <= a - i <= H - 1 and 2 <= b - j <= W - 1:
            C[(a - i, b - j)] += 1

D = Counter(v for _, v in C.items())

print((H - 2) * (W - 2) - sum(D.values()))
for i in range(1, 10):
    print(D[i])
