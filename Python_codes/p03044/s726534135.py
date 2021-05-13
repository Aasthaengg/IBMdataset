import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
edges = [[]for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    edges[u-1].append((w, v-1))
    edges[v-1].append((w, u-1))

next_v = deque([(0, 0)])
color = [-1]*n
while next_v:
    d, v = next_v.popleft()
    color[v] = d & 1
    for d2, v2 in edges[v]:
        if color[v2] != -1:
            continue
        next_v.append((d+d2, v2))
print(*color, sep='\n')
