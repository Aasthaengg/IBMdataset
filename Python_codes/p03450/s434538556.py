n,m = map(int,input().split())

from collections import defaultdict
G = defaultdict(list)

for _ in range(m):
    l,r,d = map(int,input().split())
    G[l-1].append((r-1, d))
    G[r-1].append((l-1, -d))


pos = [float("inf") for _ in range(n)]
for i in range(n):
    if pos[i] == float("inf"):
        stack = [i]
        pos[i] = 0
    while stack:
        p = stack.pop()
        for a, d in G[p]:
            if pos[a] == float("inf"):
                pos[a] = pos[p] + d
                stack.append(a)

for i in range(n):
    for to, d in G[i]:
        if pos[to] - pos[i] != d:
            print("No")
            exit()

print("Yes")

