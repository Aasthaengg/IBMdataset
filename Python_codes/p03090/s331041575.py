N = int(input())

n = N // 2
S = N + (N % 2 == 0)

groups = [[i, S - i] for i in range(1, n + 1)]

if N % 2 == 1:
    groups.append([S])

ans = []

from itertools import *

for g1, g2 in combinations(groups, 2):
    for s, t in product(g1, g2):
        ans.append((s, t))

print(len(ans))
for s, t in ans:
    print(s, t)
