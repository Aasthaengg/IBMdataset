from collections import defaultdict
import heapq
N = int(input())
graph = defaultdict(list)
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
is_visited = [False for i in range(N+1)]
q = []
heapq.heappush(q, (0, 0, 1))
t2f = {}
while q:
    c, f, t = heapq.heappop(q)
    t2f[t] = f
    if t == N:
        break
    for nt in graph[t]:
        if is_visited[nt]:
            continue
        heapq.heappush(q, (c+1, t, nt))
        is_visited[nt] = True
is_visited = [False for i in range(N+1)]
is_visited[1] = True
is_visited[N] = True
for i in range((c-1)//2):
    t = t2f[t]
    is_visited[t] = True
q = []
heapq.heappush(q, (0, 1))
ans = 0
while q:
    c, t = heapq.heappop(q)
    ans += 1
    for nt in graph[t]:
        if is_visited[nt]:
            continue
        heapq.heappush(q, (c+1, nt))
        is_visited[nt] = True
if N // 2 < ans:
    print('Fennec')
else:
    print('Snuke')