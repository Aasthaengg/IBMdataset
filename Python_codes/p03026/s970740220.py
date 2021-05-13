from collections import deque

n = int(input())
Adj_dict = {x:[] for x in range(1, n+1)}

for _ in range(n-1):
    a, b = map(int, input().split())
    Adj_dict[a].append(b)
    Adj_dict[b].append(a)
C = list(map(int, input().split()))
C = sorted(C, reverse=True)
dq_C = deque(C)

max_node = 0
max_edge_count = 0
for i in range(1,n+1):
    if len(Adj_dict[i]) >= max_edge_count:
        max_edge_count = len(Adj_dict[i])
        max_node = i

dq = deque()
dq.append(max_node)

Visited = [-1 for _ in range(n+1)]
Visited[max_node] = dq_C.popleft()
ans = 0

while dq:
    node = dq.popleft()
    Adjs = Adj_dict[node]
    for next_node in Adjs:
        if Visited[next_node] != -1:
            continue
        dq.append(next_node)
        Visited[next_node] = dq_C.popleft()
        ans += Visited[next_node]

print(ans)
print(' '.join(map(str, Visited[1:])))
