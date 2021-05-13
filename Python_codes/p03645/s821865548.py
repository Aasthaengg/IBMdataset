N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    edge[a].append(b)
    edge[b].append(a)

ans = {True: "POSSIBLE",
    False: "IMPOSSIBLE"}

print(ans[len(set(edge[0]) & set(edge[-1])) > 0])
