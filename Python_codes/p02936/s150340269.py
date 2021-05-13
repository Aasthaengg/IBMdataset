from collections import deque

n, q = list(map(int, input().split()))

adj = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

c = [0] * (n+1)

for i in range(q):
    p, x = list(map(int, input().split()))
    c[p] += x

#BFS 
q = deque([1])
visited = [False] * (n+1)
visited[1] = True


while len(q) > 0:
    v = q.popleft()
    for w in adj[v]:
        if not visited[w]:
            q.append(w)
            c[w] += c[v]
            visited[w] = True

c_str = [str(c[i+1]) for i in range(n)]
print(" ".join(c_str))

