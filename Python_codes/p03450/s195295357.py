n,m = map(int, input().split())

if m <=1:
    print("Yes")
    exit()

from collections import defaultdict
V = defaultdict(list)
 
for _ in range(m):
    a, b,c = map(int, input().split())
    V[a].append([b,c])
    V[b].append([a,-c])

inf  = float("inf") 
dist = [inf]*(n+1)

def dfs(source):
    dist[source] = 0
    q = [source]
    while q:
        a = q.pop()
        for b in V[a]:
            if dist[b[0]]!=inf:
                if dist[b[0]] != dist[a] +b[1]:
                    print("No")
                    exit()
            else:
                dist[b[0]] = dist[a] + b[1]
                q.append(b[0])

for i in range(n):
    if dist[i] ==inf:
        dfs(i)

print("Yes")