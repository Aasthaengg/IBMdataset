import itertools
from functools import reduce

N = int(input())
S = [input() for _ in range(N)]

counter = [len(list(filter(lambda s: s[0] == l, S))) for l in 'MARCH']

ans = 0
for pat in itertools.combinations(range(5), 3):
    ans += reduce(lambda a, b: a * b, [counter[p] for p in pat], 1)

print(ans)