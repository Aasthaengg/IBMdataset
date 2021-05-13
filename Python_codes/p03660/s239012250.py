import queue

N = int(input())
edges = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

from1 = [N] * N
fromN = [N] * N

que = queue.Queue()
que.put((0, 0))
while (not que.empty()):
    vertex, dist = que.get()
    if from1[vertex] != N:
        continue
    from1[vertex] = dist
    for to in edges[vertex]:
        que.put((to, dist + 1))
que.put((N - 1, 0))
while (not que.empty()):
    vertex, dist = que.get()
    if fromN[vertex] != N:
        continue
    fromN[vertex] = dist
    for to in edges[vertex]:
        que.put((to, dist + 1))

black = 0
white = 0
for i in range(N):
    if from1[i] <= fromN[i]:
        black += 1
    else:
        white += 1

print("Fennec" if black > white else "Snuke")
