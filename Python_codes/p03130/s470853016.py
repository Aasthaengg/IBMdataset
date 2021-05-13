from collections import defaultdict
d = defaultdict(int)

ab = [list(map(int, input().split())) for _ in range(3)]
for i in range(len(ab)):
    a = ab[i][0]
    b = ab[i][1]
    d[a] += 1
    d[b] += 1
x = []
for v in d.values():
    x.append(v)
if x.count(1) == 2 and x.count(2) == 2:
    print('YES')
else:
    print('NO')
