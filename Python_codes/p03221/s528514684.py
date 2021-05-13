n, m = map(int, input().split())
cnt = [[] for _ in range(n + 1)]
for i in range(m):
    p, y = map(int, input().split())
    cnt[p].append((y, i))
buf = [None] * m
for p, l in enumerate(cnt):
    if not l:
        continue
    l.sort()
    for j, (y, i) in enumerate(l):
        buf[i] = '{:06d}{:06d}'.format(p, j + 1)
print('\n'.join(buf))