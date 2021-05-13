import sys
from collections import deque
n = int(input())
graph = {i : [] for i in range(n)}
for i in range(n-1):
    a, b = [int(i) for i in sys.stdin.readline().split()]
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
c_ls = [int(i) for i in sys.stdin.readline().split()]
c_ls.sort(reverse=True)
costs = [0 for i in range(n)]
que = deque([0])
already = {0}
i = 0
while len(que) > 0:
    cur = que.popleft()
    costs[cur] = c_ls[i]
    i += 1
    for _next in graph[cur]:
        if _next not in already:
            que.append(_next)
            already.add(_next)
print(sum(c_ls[1:]))
print(" ".join([str(i) for i in costs]))