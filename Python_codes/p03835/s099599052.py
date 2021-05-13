from itertools import product

K, S = map(int, input().split())

cnt = 0
for x, y in product(range(K + 1), repeat=2):
    z = S - x - y
    if 0 <= z <= K:
        cnt += 1
print(cnt)
