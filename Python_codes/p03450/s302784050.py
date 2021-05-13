N, M, *LRD = map(int, open(0).read().split())

E = [[] for _ in range(N + 1)]
for l, r, d in zip(*[iter(LRD)] * 3):
    E[l].append((r, d))
    E[r].append((l, -d))

visited = [False] * (N + 1)
D = [0] * (N + 1)
for i in range(1, N + 1):
    if visited[i]:
        continue

    S = [i]
    while S:
        v = S.pop()
        for u, d in E[v]:
            if not visited[u]:
                visited[u] = True
                D[u] = D[v] + d
                S.append(u)

            elif D[u] != D[v] + d:
                print("No")
                quit()

print("Yes")