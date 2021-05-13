from collections import defaultdict

N = int(input())
V = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    V[a].append(b)
    V[b].append(a)

def dfs(source):
    dist = [-1]*(N+1)
    dist[source] = 0
    q = [source]
    while q:
        a = q.pop()
        for b in V[a]:
            if dist[b]!=-1:continue
            dist[b] = dist[a] + 1
            q.append(b)
    return dist

d1, d2 = dfs(1), dfs(N)
a = sum(d1[i]<=d2[i] for i in range(1, N+1))
print("Fennec" if 2*a>N else "Snuke")
