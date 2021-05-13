from collections import deque
def bfs(start, g, vals, n):
    visited = [-1]*n
    q = deque([start])
    visited[start] = 0
    while q:
        curr_node = q.popleft()
        added_val = vals[curr_node]
        for next_node in g[curr_node]:
            if visited[next_node] >= 0: continue
            visited[next_node] = visited[curr_node] + 1
            vals[next_node] += added_val
            q.append(next_node)


n,q = map(int, input().split())
g = [ [] for _ in range(n) ]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

vals = [0]*n
for _ in range(q):
    p,x = map(int, input().split())
    vals[p-1] += x

bfs(0, g, vals, n)
print(*vals)