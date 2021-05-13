h,w = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(10)]

from collections import defaultdict

V = defaultdict(list)
 
for x in range(10):
    al = ab[x]
    for y in range(10):
        V[x].append([y,al[y]])

def dfs(source):
    dist = [99]*10
    dist[source] = 0
    q = [source]
    while q:
        a = q.pop()
        for b in V[a]:
            if dist[b[0]]!=99:
                if dist[b[0]] > dist[a]+b[1]:
                    q.append(b[0])
                dist[b[0]] = min(dist[b[0]],dist[a]+b[1])
                continue
            dist[b[0]] = dist[a] + b[1]
            q.append(b[0])
    return dist

hw = [list(map(int, input().split())) for _ in range(h)]

import itertools
ss = list(itertools.chain.from_iterable(hw))

import collections
c = collections.Counter(ss)

res = 0
for i in range(10):
    res += c[i]*dfs(i)[1]

print(res)