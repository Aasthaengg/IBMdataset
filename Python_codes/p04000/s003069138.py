from collections import defaultdict

縦, 横, _, *点 = map(int, open(0).read().split())

あー = defaultdict(int)
for y, x in zip(*[iter(点)]*2):
    y -= 1; x -= 1
    for i in range(9):
        あー[y - 1 + i//3, x - 1 + i%3] += 1

答 = [0] * 10
for [y, x], c in あー.items():
    答[c] += 横 - 1 > x > 0 < y < 縦 - 1
答[0] = (縦 - 2) * (横 - 2) - sum(答)
print(*答)