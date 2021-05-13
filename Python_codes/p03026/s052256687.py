import sys

read = sys.stdin.read
readline = sys.stdin.readline

N, *abc = map(int, read().split())
c = abc[2 * (N - 1):]
c.sort()
graph = [[] for _ in range(N + 1)]
for a, b in zip(*[iter(abc[:2 * (N - 1)])] * 2):
    graph[a].append(b)
    graph[b].append(a)

nodes = [0] * (N + 1)
score = sum(c) - c[-1]
start = 1
nodes[start] = c.pop()
queue = [start]
while queue:
    V = queue.pop()
    for v in graph[V]:
        if nodes[v] == 0:
            nodes[v] = c.pop()
            queue.append(v)

print(score)
print(' '.join(map(str, nodes[1:])))
