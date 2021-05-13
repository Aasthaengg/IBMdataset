from collections import Counter
from itertools import permutations

n, c = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(c)]
a = [[] for _ in range(3)]
for i in range(n):
    for j, x in enumerate(map(lambda x: int(x)-1, input().split())):
        a[(i+j) % 3].append(x)

cnt = list(map(lambda x: Counter(x), a))
ans = float("inf")

for cp in permutations(range(c), 3):
    res = 0
    for i, x in enumerate(cp):
        for px in cnt[i].keys():
            res += d[px][x] * cnt[i][px]
    ans = min(res, ans)

print(ans)
