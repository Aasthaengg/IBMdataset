from heapq import heappush, heappop, heapreplace

INF = 10 ** 9 + 5

N, K, *TD = map(int, open(0).read().split())

E = [[] for _ in range(N)]
for t, d in zip(*[iter(TD)] * 2):
    E[t - 1].append(d)

for e in E:
    if e:
        e.sort(reverse=True)
    else:
        e.append(-INF)
E.sort(key=lambda x: -x[0])

cur = 0
Q = []
for ei in E[:K]:
    cur += ei[0]
    for eij in ei[1:]:
        heappush(Q, -eij)

for ei in E[K:]:
    for eij in ei:
        heappush(Q, -eij)

res = cur + K * K
for x in reversed(range(1, K)):
    v, w = E[x][0], -Q[0]
    if v < w:
        heappop(Q)
        cur += w
        heappush(Q, -v)
        cur -= v

    res = max(res, cur + x * x)

print(res)
