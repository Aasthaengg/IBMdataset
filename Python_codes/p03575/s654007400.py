N, M = map(int, input().split())
edges = [[] for _ in range(N)]
ans = 0

for _ in range(M):
    a, b = map(lambda n: int(n) - 1, input().split())
    edges[a].append(b)
    edges[b].append(a)

changed = True
sumi = []
count = 0
while changed:
    changed = False
    for i in range(len(edges)):
        if len(edges[i]) == 1 and i not in sumi:
            edges[edges[i][0]].remove(i)
            sumi.append(i)
            changed = True
            count += 1
print(count)