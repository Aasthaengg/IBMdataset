from collections import defaultdict
 
n = int(input())
V = defaultdict(list)

for _ in range(n-1):
    a, b,c = map(int, input().split())
    V[a].append([b,c])
    V[b].append([a,c])

def dfs(source):
    dist = [-1]*(n+1)
    dist[source] = 0
    q = [source]
    while q:
        a = q.pop()
        for b in V[a]:
            if dist[b[0]]!=-1:
                continue
            dist[b[0]] = dist[a] + b[1]
            q.append(b[0])
    return dist

q,k = map(int, input().split())
dk = dfs(k)

for i in range(q):
    x,y = map(int,input().split())
    print(dk[x]+dk[y])