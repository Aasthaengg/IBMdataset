# -*- coding: utf-8 -*-
N = int(input())

edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split(' '))
    a -= 1
    b -= 1
    edges[a].append((b, 1))
    edges[b].append((a, 1))

dists1 = [float('inf') for _ in range(N)]
used = [False for _ in range(N)]
dists1[0] = 0
used[0] = True

buf = [0]
while buf:
    src = buf.pop()
    for dst, w in edges[src]:
        if not used[dst]:
            dists1[dst] = dists1[src] + w
            used[dst] = True
            buf.append(dst)

dists2 = [float('inf') for _ in range(N)]
used = [False for _ in range(N)]
dists2[N - 1] = 0
used[N - 1] = True

buf = [N - 1]
while buf:
    src = buf.pop()
    for dst, w in edges[src]:
        if not used[dst]:
            dists2[dst] = dists2[src] + w
            used[dst] = True
            buf.append(dst)

num1, num2 = 0, 0
for d1, d2 in zip(dists1, dists2):
    if d1 <= d2:
        num1 += 1
    elif d1 > d2:
        num2 += 1

if num1 > num2:
    print('Fennec')
else:
    print('Snuke')