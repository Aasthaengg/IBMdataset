N, M = map(int, input().split())
E = [[int(x) - 1 for x in input().split()] for _ in range(M)]

ans = 0
for i in range(M):
    G = [set() for _ in range(N)]
    for j in range(M):
        if i == j:
            continue
        a, b = E[j]
        G[a].add(b)
        G[b].add(a)

    todo = [0]
    done = set()
    while todo:
        p = todo.pop()
        done.add(p)
        for np in G[p]:
            if not np in done:
                todo.append(np)

    if len(done) < N:
        ans += 1
print(ans)