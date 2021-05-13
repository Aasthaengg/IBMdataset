from collections import Counter

H, W, N, *AB = map(int, open(0).read().split())

move = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),  (0, 0),  (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

C = Counter()
for a, b in zip(*[iter(AB)] * 2):
    C.update(
        (a - i, b - j)
        for i, j in move
        if 2 <= a - i <= H - 1 and 2 <= b - j <= W - 1
    )

D = [0] * 10
for v in C.values():
    D[v] += 1

D[0] = (H - 2) * (W - 2) - len(C)
print("\n".join(map(str, D)))
