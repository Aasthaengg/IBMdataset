from collections import Counter
n,k,l = map(int,input().split())
e1 = [[] for _ in range(n)]
e2 = [[] for _ in range(n)]

for _ in range(k):
    p,q = map(int,input().split())
    e1[p-1].append(q-1)
    e1[q - 1].append(p - 1)

for _ in range(l):
    p,q = map(int,input().split())
    e2[p-1].append(q-1)
    e2[q - 1].append(p - 1)

g1 = [-1]*n
for i in range(n):
    if g1[i] != -1:
        continue
    g1[i] = i
    s = [i]
    while s:
        v = s.pop()
        for d in e1[v]:
            if g1[d] != -1:
                continue
            g1[d] = i
            s.append(d)
g2 = [-1]*n
for i in range(n):
    if g2[i] != -1:
        continue
    g2[i] = i
    s = [i]
    while s:
        v = s.pop()
        for d in e2[v]:
            if g2[d] != -1:
                continue
            g2[d] = i
            s.append(d)
g = []
for i in range(n):
    g.append((g1[i], g2[i]))
c = Counter(g)
f = [c[g[i]] for i in range(n)]
print(' '.join(map(str, f)))