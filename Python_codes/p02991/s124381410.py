from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    _from, to = map(int, input().split())
    edges[_from-1].append(to-1)

start, goal = map(int, input().split())

todo = deque([])
seen = [[False] * n for i in range(3)]
seen[0][start-1] = True
for to in edges[start-1]:
    dim = 1
    dist = 1
    todo.append([to, dim, dist])

while todo:
    node, dim, dist = todo.popleft()
    if seen[dim][node]:
        continue
    seen[dim][node] = True
    dim += 1
    if dim == 3:
        dim = 0
    for to in edges[node]:
        if seen[dim][to]:
            continue
        todo.append([to, dim, dist+1])
        if to == goal-1 and dim == 0:
            print((dist+1)//3)
            exit()

print(-1)