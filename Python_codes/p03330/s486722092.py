from itertools import product
from collections import Counter
N, C = map(int, input().split())
D = [tuple(map(int, input().split())) for _ in range(C)]

color = [[] for _ in range(3)]
for i in range(N):
    inp = tuple(map(int, input().split()))
    for j, c in enumerate(inp):
        color[(i + j) % 3].append(c-1)

cnt = [Counter(color[i]) for i in range(3)]


def point(d, col):
    res = 0
    for k, v in d.items():
        res += D[k][col] * v
    return res


ans = 10**9
for xyz in product(range(C), repeat=3):
    if len(set(xyz)) != 3:
        continue
    tmp = sum(point(cnt[i], xyz[i]) for i in range(3))
    ans = min(ans, tmp)

print(ans)
