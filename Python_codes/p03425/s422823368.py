from itertools import combinations

n = int(input())
s = [input() for _ in range(n)]

d = dict()
for name in s:
    if name[0] not in d:
        d[name[0]] = 1
    else:
        d[name[0]] += 1

res = 0
for v in combinations(['M', 'A', 'R', 'C', 'H'], 3):
    if v[0] in d and v[1] in d and v[2] in d:
        res += d[v[0]] * d[v[1]] * d[v[2]]

print(res)