from collections import deque
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
cnt = [1, 1]
q = deque([(0, 0), (n-1, 1)])
seen = [False]*n
seen[0] = seen[n-1] = True
while q:
    node, turn = q.popleft()
    for c_node in graph[node]:
        if seen[c_node]:
            continue
        seen[c_node] = True
        cnt[turn] += 1
        q.append((c_node, turn))
print('FSennunkeec'[cnt[1]>=cnt[0]::2])