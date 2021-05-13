import sys
import math
import fractions
from collections import deque
from collections import defaultdict
sys.setrecursionlimit(10**7)

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

c = list(map(int, input().split()))
c.sort(reverse=True)
sum_val = sum(c) - max(c)

assign = [0] * N
index = 0

q = deque()
q.append(0)
visited = []

while len(q) != 0:
    cur = q.popleft()
    assign[cur] = c[index]
    index += 1
    for n in graph[cur]:
        if n not in visited:
            q.append(n)
    visited.append(cur)

print(sum_val)
print(" ".join(map(str, assign)))
