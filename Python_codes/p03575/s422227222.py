from collections import deque

n, m = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(m)]
d = {i: [] for i in range(1, n+1)}
for a, b in L:
    d[a].append(b)
    d[b].append(a)
cnt = 0
for a, b in L:
    d[a].remove(b)
    d[b].remove(a)
    ds = {i: -1 for i in range(1, n+1)}
    ds[1] = 0
    q = deque([1])
    while q:
        t = q.popleft()
        for v in d[t]:
            if ds[v] < 0:
                ds[v] += 1
                q.append(v)
    if -1 in ds.values():
        cnt += 1
    d[a].append(b)
    d[b].append(a)
print(cnt)
