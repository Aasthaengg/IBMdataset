n = int(input())

deg = [0 for i in range(n)]

from collections import defaultdict
G = defaultdict(list)


abl = []
for _ in range(n-1):
    a,b = map(int,input().split())
    deg[a-1] += 1
    deg[b-1] += 1
    abl.append((a-1, b-1))
    G[a-1].append(b-1)
    G[b-1].append(a-1)

cl = list(map(int,input().split()))
cl = sorted(cl)
ansl = [0 for _ in range(n)]
for c in cl:
    for idx, d in enumerate(deg):
        if d == 1:
            ansl[idx] = c
            deg[idx] -= 1
            for j in G[idx]:
                deg[j] -= 1
            break
for idx, a in enumerate(ansl):
    if a == 0:
        ansl[idx] = cl[-1]

print(sum(cl[:-1]))
print(*ansl)


