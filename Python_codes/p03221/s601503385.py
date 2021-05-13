from collections import Counter

N, M = map(int, input().split(' '))
records = [tuple(map(int, input().split(' '))) for _ in range(M)]
s_records = sorted(records)

counter = Counter()
d = {}

for p, y in s_records:
    counter[p] += 1
    d[(p, y)] = '{:06}{:06}'.format(p, counter[p])

for p, y in records:
    print(d[(p, y)])
