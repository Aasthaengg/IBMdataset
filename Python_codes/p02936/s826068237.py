n, q = list(map(int, input().split()))

adj = [[] for _ in range(n)]

for i in range(n-1):
    a, b = list(map(int, input().split()))

    adj[b-1].append(a-1)
    adj[a-1].append(b-1)

cnt = [0] * n
for i in range(q):
    p, x = list(map(int, input().split()))

    cnt[p-1] += x

counter = [0] * n
visited = [True] + [False] * (n-1)
visit = [0]

while len(visit) > 0:
    node = visit.pop()
    counter[node] += cnt[node]

    for adjNode in adj[node]:
        if visited[adjNode] == False:
            visited[adjNode] = True
            visit.append(adjNode)

            counter[adjNode] += counter[node]

print(" ".join(map(str, counter)))