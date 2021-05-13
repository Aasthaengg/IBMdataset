from collections import defaultdict
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
if m == 0:
    print('Yes')
    exit()
edges = defaultdict(list)

for i in range(m):
    left, right, dist = map(int, input().split())
    edges[left-1].append((right-1, dist))
    edges[right-1].append((left-1, -dist))

seen = [None] * n
for node in range(n):
    if seen[node] is not None:
        continue

    seen[node] = 0
    todo = []
    while edges[node]:
        to, dis = edges[node].pop()
        seen[to] = dis
        todo.append([to, dis])

    while todo:
        new, dis = todo.pop()

        while edges[new]:
            to, n_dis = edges[new].pop()
            if seen[to] is None:
                seen[to] = dis + n_dis
            elif seen[to] != dis + n_dis:
                print('No')
                exit()
            todo.append([to, dis + n_dis])

print('Yes')
