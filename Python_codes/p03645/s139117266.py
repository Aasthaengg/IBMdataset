N, M = map(int, input().split())

adj = [set() for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].add(b)
    adj[b].add(a)

if len(adj[0] & adj[N - 1]) > 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")