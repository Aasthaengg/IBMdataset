from collections import deque

n = int(input())
g = [None] * n
visited = [0] * n
dist = [-1] * n
Q = deque()

while n:
    l = list(map(int, input().split()))
    g[l[0]-1] = [i-1 for i in l[2:]]
    n -= 1

Q.append((0, 0)) 
visited[0] = 1

while Q:
    i, d = Q.popleft()         
    dist[i] = d
    for c in g[i]:
        if not visited[c]:
            visited[c] = 1
            Q.append((c, d+1))

for i, d in enumerate(dist):
    print(i+1, d)
