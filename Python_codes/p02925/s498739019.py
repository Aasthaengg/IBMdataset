import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
pair = N * (N - 1) // 2
ptoi = dict()

i = 0
for x in range(1, N):
    for y in range(x + 1, N + 1):
        ptoi[(x, y)] = i
        ptoi[(y, x)] = i
        i += 1

edge = [[] for _ in range(pair)]
indeg = [0] * pair
for i in range(1, N+1):
    inp = list(map(int, input().split()))
    for s, t in zip(inp[:-1], inp[1:]):
        edge[ptoi[(i, s)]].append(ptoi[(i, t)])
        indeg[ptoi[(i, t)]] += 1


now = [i for i, d in enumerate(indeg) if d == 0]
day = 0
while now:
    nxt = []
    while now:
        s = now.pop()
        for t in edge[s]:
            if indeg[t] <= 0:
                continue
            indeg[t] -= 1
            if indeg[t] == 0:
                nxt.append(t)
    day += 1
    now = nxt

if all(i <= 0 for i in indeg):
    print(day)
else:
    print(-1)