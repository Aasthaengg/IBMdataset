n,m = map(int, input().split())

ab = [list(map(int, input().split())) for _ in range(m)]


def dfs(source):
    dist = [-1]*(n+1)
    dist[source] = 0
    q = [source]
    while q:
        a = q.pop()
        for b in V[a]:
            if dist[b]!=-1:
                continue
            dist[b] = dist[a] + 1
            q.append(b)
    return dist

from collections import defaultdict
import collections

res = 0
for i in range(m):
    abc = ab.copy()
    del abc[i]
    V = defaultdict(list)

    for _ in range(m-1):
        a, b = abc[_][0],abc[_][1]
        V[a].append(b)
        V[b].append(a)
    d1 =dfs(1)
    c = collections.Counter(d1)
    if c[-1] >1:
        res +=1
print(res)