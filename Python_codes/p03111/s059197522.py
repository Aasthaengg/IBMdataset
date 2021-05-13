from itertools import product

n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]

ans = 10 ** 10
for bit in product([0, 1, 2, 3], repeat=n):
    tmp = [0] * 4
    mp = 0
    for i, j in enumerate(bit):
        if j != 3 and tmp[j] != 0:
            mp += 10
        tmp[j] += l[i]
    if any([i == 0 for i in tmp[:3]]):
        continue
    mp += abs(a - tmp[0]) + abs(b - tmp[1]) + abs(c - tmp[2])
    ans = min(ans, mp)
print(ans)
