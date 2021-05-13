import sys
read = sys.stdin.readline

n = int(read())
V = 1001000

g = [[] for _ in range(V)]
deg = [0] * V
vlist = set()

for i in range(1, n + 1):
    a = list(map(int, read().rstrip().split()))
    for j in range(n - 2):
        v1 = min(i, a[j]) * 1001 + max(i, a[j])
        v2 = min(i, a[j + 1]) * 1001 + max(i, a[j + 1])
        vlist.add(v1)
        vlist.add(v2)
        g[v1].append(v2)
        deg[v2] += 1

d = [0] * V
check_cnt = 0
q = []
for v in vlist:
    if deg[v] == 0:
        q.append(v)

if len(q) == 0:
    print(-1)
    exit()

for v in q:
    check_cnt += 1
    for nv in g[v]:
        d[nv] = max(d[nv], d[v] + 1)
        deg[nv] -= 1
        if deg[nv] == 0:
            q.append(nv)
if check_cnt == n * (n - 1) // 2:
    print(max(d) + 1)
else:
    print(-1)
