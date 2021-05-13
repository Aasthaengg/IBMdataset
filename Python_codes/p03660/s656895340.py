from collections import deque
n = int(input())
edges = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)
ans = [0] * n
ans[0] = 1
ans[-1] = -1
Q = deque([0, n - 1])
while Q:
    p = Q.popleft()
    cur = ans[p]
    for v in edges[p]:
        if ans[v] == 0:
            ans[v] = cur
            Q.append(v)
if ans.count(1) > ans.count(-1):
    print("Fennec")
else:
    print("Snuke")