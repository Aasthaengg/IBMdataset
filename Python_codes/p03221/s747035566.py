n, m = map(int, input().split())
ans = ['']*m
mat = [list(map(int, input().split())) for _ in range(m)]
d = {}
for idx in range(m):
    p, y = mat[idx]
    y = (y, idx)
    ans[idx] += str(p).zfill(6)
    if p in d:
        d[p].append(y)
    else:
        d[p] = [y]

for v in d.values():
    v.sort(key=lambda x: x[0])
    for i, (_, idx) in enumerate(v):
        i += 1
        ans[idx] += str(i).zfill(6)

for a in ans:
    print(a)