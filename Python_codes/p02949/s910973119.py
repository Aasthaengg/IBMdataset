import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N, M, P = map(int, input().split())
edge = [[] for _ in range(N + 1)]
ein = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edge[a].append((b, P - c))
    ein[b].append(a)

# 到達できる地点を決める
reach1 = [False] * (N + 1)
reach1[1] = True
node = [1]
while node:
    s = node.pop()
    for t, _ in edge[s]:
        if not reach1[t]:
            reach1[t] = True
            node.append(t)

reach2 = [False] * (N + 1)
reach2[N] = True
node = [N]
while node:
    s = node.pop()
    for t in ein[s]:
        if not reach2[t]:
            reach2[t] = True
            node.append(t)

can_go = []
Vertices = []
for i, (x, y) in enumerate(zip(reach1, reach2)):
    can_go.append(x & y)
    if x & y:
        Vertices.append(i)


inf = 10**18
cost = [inf] * (N + 1)
cost[1] = 0
for _ in range(M + 5):
    update = False
    for s in Vertices:
        now = cost[s]
        for t, c in edge[s]:
            if not can_go[t]:
                continue
            if cost[t] > now + c:
                cost[t] = now + c
                update = True


if update:
    print(-1)
else:
    print(max(0, -cost[N]))