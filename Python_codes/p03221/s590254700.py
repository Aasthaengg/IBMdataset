from collections import defaultdict
d = defaultdict(list)


def sortpy(y):
    return {x: i for i, x in enumerate(sorted(y), 1)}


n, m = map(int, input().split())
py = [[int(x) for x in input().split()] for _ in range(m)]

for p, y in py:
    d[p].append(y)

nd = {p: sortpy(y) for p, y in d.items()}

for p, y in py:
    print('{:06g}{:06g}'.format(p, nd[p][y]))