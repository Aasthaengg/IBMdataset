from collections import defaultdict
n, m = map(int, input().split())

d = defaultdict(list)
for i in range(m):
    p, y = map(int, input().split())
    d[p].append([i, y])

for i in range(1, n + 1):
    tmp = d[i]
    tmp.sort(key=lambda x: x[1])
    for i, j in enumerate(tmp):
        j.append(i + 1)

ans = []
for a, b in d.items():
    for i in b:
        i.append(a)
        ans.append(i)

for _, _, c, p in sorted(ans):
    print("{:06}{:06}".format(p, c))