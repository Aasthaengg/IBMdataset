N, M = map(int, input().split())
AB = []
ans = 0

for _ in range(M):
    Ai, Bi = map(int, input().split())
    AB.append((Ai,Bi))

for i in range(M):
    memo = [[] for _ in range(N+1)]
    for j in range(M):
        if i != j:
            memo[AB[j][0]].append(AB[j][1])
            memo[AB[j][1]].append(AB[j][0])
    queue = [1]
    visited = [0] * (N+1)

    while queue:
        node = queue.pop()
        next_nodes = memo[node]
        for next_node in next_nodes:
            if visited[next_node] == 0:
                queue.append(next_node)
        visited[node] = 1

    if sum(visited[1:]) != N:
        ans += 1

print(ans)
