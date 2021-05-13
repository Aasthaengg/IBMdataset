from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
edges = [[] for i in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

todo = deque([(0, 1), (n-1, 2)])

colors = [0] * n
colors[0] = 1
colors[-1] = 2

while todo:
    node, color = todo.popleft()
    for to in edges[node]:
        if colors[to]:
            continue
        else:
            colors[to] = color
            todo.append((to, color))

fennec_count = colors.count(1)
if fennec_count > n // 2:
    print('Fennec ')

else:
    print('Snuke ')
