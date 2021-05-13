import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

S, T = map(int, input().split())

inf = 10**6
ans = [[inf, inf, inf] for i in range(N+1)]

q = deque([S])
ans[S][0] = 0
while q:
    now = q.popleft()
    for next in graph[now]:
        flag = 0
        for i in range(3):
            if ans[now][i] != inf:
                if ans[next][(i+1)%3] > ans[now][i] + 1:
                    flag = 1
                    ans[next][(i+1)%3] = ans[now][i] + 1
        if flag == 1:
            q.append(next)

if ans[T][0] == inf:
    print(-1)
else:
    print(ans[T][0]//3)
