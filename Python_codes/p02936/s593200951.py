from collections import defaultdict

N, Q = map(int, input().split())
d = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

c = defaultdict(int)

for _ in range(Q):
    p, x = map(int, input().split())
    c[p] += x

ans = [0 for i in range(N)]
que = [(1, 0, -1)]
while len(que) > 0:
    tmp = []
    for v, x, par in que:
        x += c[v]
        ans[v - 1] = str(x)
        for w in d[v]:
            if w != par:
                tmp.append((w, x, v))
    que = tmp

print(*ans)
