from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
roots = [[] for _ in range(n)]
signs = [-1 for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    roots[a].append(b)
    roots[b].append(a)

queue = deque([0])
signs[0] = 0

while queue:
    room = queue.popleft()
    for root in roots[room]:
        if signs[root] == -1:
            signs[root] = room
            queue.append(root)

print('Yes')
for i in signs[1:]:
    print(i + 1)
