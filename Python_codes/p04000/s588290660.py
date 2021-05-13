from collections import Counter
from itertools import product

H, W, N, *AB = map(int, open(0).read().split())

C = Counter()
for a, b in zip(*[iter(AB)] * 2):
    C.update(
        (a - i, b - j)
        for i, j in product((-1, 0, 1), repeat=2)
        if 2 <= a - i <= H - 1 and 2 <= b - j <= W - 1
    )

D = Counter(v for _, v in C.items())

print((H - 2) * (W - 2) - sum(D.values()))
for i in range(1, 10):
    print(D[i])
